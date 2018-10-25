from app import app

app.config['SECRET_KEY'] = 'mysecret@12345'

if __name__ == '__main__':
	app.run(debug=True)