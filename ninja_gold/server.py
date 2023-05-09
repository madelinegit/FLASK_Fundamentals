from flask import Flask, request, redirect, render_template, query, session

import random

app = Flask(__name__)

app.secret_key = "Py Gold Mine"

@app.route('/')
def index():
    if 'earnings' and 'gold_log' not in session:
        session['gold_log']=[]
        session['earnings'] = 0
    print('it works! keep coding')
    query = gold_log.query.order_by(gold_log.id.desc())
    return render_template('index.html')
#creates mini instance of a user

@app.route('/ninja_gold', methods=['POST'])
def calculate():
    if 'is-a-farmer' == request.form['money']:
    #request.form money references the hidden value money
        mine_yeild = random.randint(10, 20)
        session['earnings'] += mine_yeild
        print("mine_yeild")
        session['gold_log'].append(f'Earned {mine_yeild} from the farm!')
        return redirect('/')

    if 'is-a-caveman' == request.form['money']:
    #request.form money references the hidden value money
        mine_yeild = random.randint(5, 10)
        session['earnings'] += mine_yeild
        print("mine_yeild")
        session['gold_log'].append(f'Earned {mine_yeild} from the cave!')
        return redirect('/')

    if 'is-a-homeowner' == request.form['money']:
        #request.form money references the hidden value money
        mine_yeild = random.randint(5, 10)
        session['earnings'] += mine_yeild
        print("mine_yeild")
        session['gold_log'].append(f'Earned {mine_yeild} from home!')
        return redirect('/')

    if 'is-a-gambler' == request.form['money']:
        #request.form money references the hidden value money
        mine_yeild = random.randint(-5, 10)
        session['earnings'] += mine_yeild
        print("mine_yeild")
        session['gold_log']
        if (mine_yeild > 0):
            session['gold_log'].append(f'Earned {mine_yeild} at the casino!')
            print('OK')
        if (mine_yeild < 0):
            session['gold_log'].append(f'Lost {mine_yeild} at the casino!')
            print('OK')
        return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')
#Reset Button

if __name__=='__main__':
    app.run(debug=True)

#color coat the positives and negatives
# make the list look good and not like a tuple
