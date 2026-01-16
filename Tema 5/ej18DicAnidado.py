datosCliente= {
    "nombre":"Carlos",
    "contacto": {
        "email": "carlos@ejemplo.com",
        "telefon":"555-1234",
    },
    "pedidos":[
        {"id":"P001", "total":54.78},
        {"id": "P002", "total": 23.54}

    ]
}
#mostrar email
email_cliente = datosCliente["contacto"]["email"]
print(f"Email:{email_cliente}")

#acceder total del primer pedido
totalPedido = datosCliente["pedidos"][0]["total"]
print(f"Toatal Pedido 1:{totalPedido}")
