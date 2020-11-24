class CSP:
    def select_unassigned_variable(self, board):
        raise NotImplementedError('Implement in a subclass')

    def valid_inference(self, var, value):
        raise NotImplementedError('Implement in a subclass')

    def order_domain_values(self, var, board):
        raise NotImplementedError('Implement in a subclass')


class CSPSolver:
    def solve(self, board, csp):
        raise NotImplementedError('Implement in a subclass')
