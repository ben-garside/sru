import ssl

# SSL CONTEXT for HTTPS
def ssl_context(ssl_cert, ssl_key):
    sslContext = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    sslContext.load_cert_chain(ssl_cert, ssl_key)
    return sslContext