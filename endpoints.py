from flask import jsonify, request


class CalculatorEndpoints:
    #Clase para registrar los endpoints de la calculadora.

    def __init__(self, app, calculator):
        self.app = app
        self.calculator = calculator
        self.register_routes()

    def register_routes(self):
        @self.app.route('/calc/add')
        def add():
            try:
                a, b = self._get_params()
            except ValueError as exc:
                return jsonify(error=str(exc)), 400
            return jsonify(result=self.calculator.add(a, b), operation='add')

        @self.app.route('/calc/subtract')
        def subtract():
            try:
                a, b = self._get_params()
            except ValueError as exc:
                return jsonify(error=str(exc)), 400
            return jsonify(result=self.calculator.subtract(a, b), operation='subtract')

        @self.app.route('/calc/multiply')
        def multiply():
            try:
                a, b = self._get_params()
            except ValueError as exc:
                return jsonify(error=str(exc)), 400
            return jsonify(result=self.calculator.multiply(a, b), operation='multiply')

        @self.app.route('/calc/divide')
        def divide():
            try:
                a, b = self._get_params()
                value = self.calculator.divide(a, b)
            except ValueError as exc:
                return jsonify(error=str(exc)), 400
            return jsonify(result=value, operation='divide')

        @self.app.route('/calc/power')
        def power():
            try:
                a, b = self._get_params()
            except ValueError as exc:
                return jsonify(error=str(exc)), 400
            return jsonify(result=self.calculator.power(a, b), operation='power')

    def _get_params(self):
        try:
            a = float(request.args.get('a', ''))
            b = float(request.args.get('b', ''))
        except ValueError:
            raise ValueError('Parámetros inválidos. Usa ?a=numero&b=numero')
        return a, b
