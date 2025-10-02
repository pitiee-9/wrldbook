from flask import Flask, Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, Post
from . import db
import json
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    main_posts = Post.query.filter_by(parent_id=None).order_by(Post.date.desc()).all()
    
    if request.method == 'POST': 
        post_content = request.form.get('post_content')
        
        if len(post_content) < 1:
            flash('Post is too short!', category='error') 
        else:
            new_post = Post(data=post_content, user_id=current_user.id, date=datetime.now())
            db.session.add(new_post)
            db.session.commit()
            flash('Message posted!', category='success')
            return redirect(url_for('views.home'))

    return render_template("home.html", user=current_user, posts=main_posts)
@views.route('/create-reply/<int:post_id>', methods=['POST'])
@login_required
def create_reply(post_id):
    reply_content = request.form.get('reply_content')
    
    if len(reply_content) < 1:
        flash('Reply is too short!', category='error')
    else:
        new_reply = Post(
            data=reply_content,
            user_id=current_user.id, 
            date=datetime.now(),
            parent_id=post_id
        )
        db.session.add(new_reply)
        db.session.commit()
        flash('Reply added!', category='success')
    
    return redirect(url_for('views.home'))

@views.route('/private-notes')
@login_required
def private_notes():
    if request.method == 'POST': 
        note = request.form.get('note')
        
        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Private note added!', category='success')

    return render_template("private_notes.html", user=current_user)

@views.route('/delete-post', methods=['POST'])
@login_required
def delete_post():
    post_data = json.loads(request.data)
    post_id = post_data['postId']
    post = Post.query.get(post_id)
    
    if post:
        # to allow deletion only if user owns the post or is admin
        if post.user_id == current_user.id:
            replies = Post.query.filter_by(parent_id=post_id).all()
            for reply in replies:
                db.session.delete(reply)
            
            db.session.delete(post)
            db.session.commit()
            flash('Post deleted!', category='success')
    
    return jsonify({})

@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    note = json.loads(request.data)
    note_id = note['noteId']
    note = Note.query.get(note_id)
    
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})