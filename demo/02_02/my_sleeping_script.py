import time
import pickle

file_name = '/app/pickle/counter.pickle'

try:
    with open(file_name, 'rb') as counter_file:
        counter = pickle.load(counter_file)
except:
    counter = 1

while True:
    time.sleep(1)
    print(counter)
    counter += 1
    with open(file_name, 'wb') as counter_file:
        pickle.dump(counter, counter_file)
