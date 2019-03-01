from flask_restplus import Namespace, fields

api = Namespace('Payments', 'Payment Related APIs', path='/payments')

a_stripe_details = api.model('Charge Details',
                             {'id': fields.Integer(),
                              'paymentReference': fields.String(),
                              'bookingReference': fields.String(),
                              'paymentFor': fields.String()
                             })

a_create_stripe_charges = api.model('Create Charges',
                                    {
                                     'referenceNumber': fields.String(),
                                     'token': fields.String(),
                                     'email': fields.String(),
                                     'amount': fields.Decimal(),
                                     'description': fields.String(),
                                     'paymentFor': fields.String()
                                     })