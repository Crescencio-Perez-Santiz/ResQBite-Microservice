from Infrastructure.Routers.router import create_app
import ssl

app = create_app()

if __name__ == '__main__':
    print("Iniciando la aplicación...")
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(certfile='fullchain.pem', keyfile='privkey.pem')
    app.run(host='0.0.0.0', port=5003, ssl_context=context, debug=True)
