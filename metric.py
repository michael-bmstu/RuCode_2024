from sklearn.metrics import mean_absolute_percentage_error as mape
import numpy as np

class MyMAPE:
    @staticmethod
    def mape(y_t, y_p):
        return mape(y_t, y_p)
    
    def get_final_error(self, error, weight):
        return error
    
    def is_max_optimal(self):
        # the larger metric value the better
        return False

    def evaluate(self, y_p, y_t, weight):
        score = self.mape(np.exp(y_t), np.exp(y_p[0]))
        return score, 0