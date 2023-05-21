# -*- coding: utf-8 -*-
from datetime import time

from odoo import models, fields, api

import paho.mqtt.client as paho

class SaleOrder(models.Model):
    _name = 'sales.id'
    _description = 'Sale ID'

    sale_order_id = fields.Many2one('sale.order.line', string='Sale Order')
    product_count = fields.Float(string='Product Count', related='sale_order_id.product_uom_qty', readonly=True)
    state = fields.Integer(string='state')

    @api.one
    def update_variable(self):
        self.state = 2
    # client1.connect(broker, port)  # establish connection
    def iniciar(self):
        broker = "192.168.204.110"
        port = 1884

        def on_publish(client, userdata, result):  # create function for callback
            print("data published \n")
            pass

        client2 = paho.Client("riba_PC")  # create client objectç

        def on_message(client, userdata, message):
            broker = "192.168.204.110"
            port = 1884

            def on_publish(client, userdata, result):  # create function for callback
                print("data published \n")
                pass

            client1 = paho.Client("192.168.204.110")  # create client objectç
            client1.connect(broker, port)  # establish connectio
            client1.on_publish = on_publish  # assign function to callback
            if message.payload.decode().strip('{}') == 'A5':

                client1.publish("Microdesys/f/m1command", "m1reset")

            if message.payload.decode().strip('{}') == 'P1':
                self.update_variable()
                client1.publish("Microdesys/f/m1command", "m1reset")
            client1.disconnect()
            return True

        client2.on_message = on_message
        client2.connect(broker, port)  # establish connection
        client2.subscribe("Microdesys/f/m1command")
        client2.loop_start()

    def fer_2_peces(self):
        broker = "192.168.204.110"
        port = 1884

        def on_publish(client, userdata, result):  # create function for callback
            print("data published \n")
            pass

        client1 = paho.Client("192.168.204.110")  # create client objectç
        client1.connect(broker, port)  # establish connection
        client1.on_publish = on_publish  # assign function to callback
        if self.product_count < 10:
            numero = "0" + str(self.product_count).split(".")[0]
        else:
            numero = str(self.product_count).split(".")[0]
        client1.publish("Microdesys/f/m1command", "m1produce" + numero)  # publish

    def fer_infinites(self):
        broker = "192.168.204.110"
        port = 1884

        def on_publish(client, userdata, result):  # create function for callback
            print("data published \n")
            pass

        client1 = paho.Client("192.168.204.110")  # create client objectç
        client1.connect(broker, port)  # establish connection
        client1.on_publish = on_publish  # assign function to callback
        client1.publish("Microdesys/f/m1command", "m1produce00")  # publish

    def arrancar(self):
        broker = "192.168.204.110"
        port = 1884

        def on_publish(client, userdata, result):  # create function for callback
            print("data published \n")
            pass

        client1 = paho.Client("192.168.204.110")  # create client objectç
        client1.connect(broker, port)  # establish connection
        client1.on_publish = on_publish  # assign function to callback
        client1.publish("Microdesys/f/m1command", "m1start")  # publish

    def parar(self):
        broker = "192.168.204.110"
        port = 1884

        def on_publish(client, userdata, result):  # create function for callback
            print("data published \n")
            pass

        client1 = paho.Client("192.168.204.110")  # create client objectç
        client1.connect(broker, port)  # establish connection
        client1.on_publish = on_publish  # assign function to callback
        client1.publish("Microdesys/f/m1command", "m1stop")  # publish
        return True

    def reset(self):
        broker = "192.168.204.110"
        port = 1884

        def on_publish(client, userdata, result):  # create function for callback
            print("data published \n")
            pass

        client1 = paho.Client("192.168.204.110")  # create client objectç
        client1.connect(broker, port)  # establish connection
        client1.on_publish = on_publish  # assign function to callback
        client1.publish("Microdesys/f/m1command", "m1reset")  # publish
        return True

    def emergencia(self):
        broker = "192.168.204.110"
        port = 1884

        def on_publish(client, userdata, result):  # create function for callback
            print("data published \n")
            pass

        client1 = paho.Client("192.168.204.110")  # create client objectç
        client1.connect(broker, port)  # establish connection
        client1.on_publish = on_publish  # assign function to callback
        client1.publish("Microdesys/f/m1command", "m1emer")  # publish
        return True
