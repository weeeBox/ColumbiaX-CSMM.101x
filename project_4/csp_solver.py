class CSP:
    def __init__(self, select_unassigned_variable, order_domain_values, valid_inference):
        self.select_unassigned_variable = select_unassigned_variable
        self.order_domain_values = order_domain_values
        self.valid_inference = valid_inference


class CSPSolver:
    def solve(self, board, csp):
        raise NotImplementedError('Implement in a subclass')
