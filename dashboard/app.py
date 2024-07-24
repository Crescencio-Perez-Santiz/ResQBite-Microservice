from Infrastructure.Routers.router import create_app

app = create_app()

if __name__ == '__main__':
    print("Iniciando la aplicación...")
    app.run(debug=True)
