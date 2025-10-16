from website import app

# Vercel requires this
if __name__ == '__main__':
    app.run()
else:
    # For Vercel serverless
    application = app