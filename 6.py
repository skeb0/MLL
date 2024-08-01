!pip install pgmpy

import pandas as pd
data = pd.read_csv('datasetheart.csv', names=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'RESULT'])

from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination
from pgmpy.estimators import MaximumLikelihoodEstimator

model = BayesianModel([("A","B"),("B","C"),("C","D"),("D","RESULT")])
model.fit(data,estimator=MaximumLikelihoodEstimator)

infer = VariableElimination(model)
q = infer.query(variables=['RESULT'],evidence={"C":"2"})
print(q)
