import utils 
from flask import Flask, render_template, render_template_string, jsonify, request, send_from_directory, redirect, url_for
import json
import os
app = Flask(__name__)


branches_list = ['Yishun', 'ToaPayoh', 'Bishan', 'JurongEast']
queue = [
    {
        "type": "priority",
        "counter": 0,
        "queue": [],
        "hold_queue": [],
        "pause_queue":  False 
    },
    {
        "type": "personal",
        "counter": 0,
        "queue": [],
        "hold_queue": [],
        "pause_queue": False
    },
    {
        "type": "corporate",
        "counter": 0,
        "queue": [],
        "hold_queue": [],
        "pause_queue": False
    }
]

queue_list = {branch:{} for branch in branches_list}

################## Customer ##################
@app.route('/customer', methods=['GET'])
def customer():
    return render_template('Customer.html', branches_list = branches_list)

@app.route('/customer/queue', methods=['GET'])
def customerqueue():
    branch = request.args.get('branch')
    cust_type=request.args.get('cust_type')
    #Check if file available, else new file created
    file_data = utils.extract_data(branch, queue)
    #Generate message for customer display
    message = utils.addNewqueue(file_data, cust_type, branch)
    return render_template('Customer.html', branches_list = branches_list,
                                           branch=branch,
                                           message=message)


################## CRO ##################
@app.route('/cro', methods=['GET'])
def cro():
    return render_template('CRO.html', branches_list = branches_list)


#API for displaying, clearing and holding queue 
@app.route('/cro/handle_q', methods=['GET'])
def displayQueue():
    branch = request.args.get('branch')
    btn = request.args.get('btn')
    
    #if clear queue is selected 
    if btn == 'Clear Queue':
        q_clear_notif = utils.clear_queue(branch)
        return render_template('CRO.html', branches_list = branches_list, 
                                        branch = branch,
                                        q_clear_notif = q_clear_notif)
    
    #Consisting of both display queue and hold queue here
    else:
        #Check if file available, else new file created
        file_data = utils.extract_data(branch, queue)
        
        #To display queue. Utils function to format message nicely 
        if btn == 'Display Queue':
            priority_q = utils.display_q_message('priority', file_data)
            personal_q = utils.display_q_message('personal', file_data)
            corporate_q = utils.display_q_message('corporate', file_data)
   
            return render_template('CRO.html', branches_list = branches_list, 
                                    branch = branch,
                                    priority_q = priority_q, 
                                    personal_q = personal_q,
                                    corporate_q = corporate_q)
        
        #List of all the buttons for hold and initiate queue for looping 
        hold_init_btn = ['priority_btn', 'personal_btn', 'corporate_btn']
        
        for q_btn in hold_init_btn:        
            #if a button for hold or initiate queue is clicked 
            if request.args.get(q_btn) is not None:
                #looping within file to extract the right queue based
                #on the button name which has been selected 
                for i in range(len(file_data)):
                    if file_data[i]['type'] == q_btn.split("_")[0]:
                        #Change file data based on selection 
                        if request.args.get(q_btn) == 'Hold Queue':
                            file_data[i]["pause_queue"] = True
                        else:
                            file_data[i]["pause_queue"] = False
                #file update
                utils.write_file(branch, file_data)
                
                #Updating display of queue status 
                priority_q = utils.display_q_message('priority', file_data)
                personal_q = utils.display_q_message('personal', file_data)
                corporate_q = utils.display_q_message('corporate', file_data)
            
                return render_template('CRO.html', branches_list = branches_list, 
                                        branch = branch,
                                        priority_q = priority_q, 
                                        personal_q = personal_q,
                                        corporate_q = corporate_q)

                
################## Counter ##################
@app.route('/counter', methods=['GET'])
def counter_main():
    counter_list = [i for i in range(1,20)]
    return render_template('CounterMain.html', branches_list = branches_list, 
                                               counter_list = counter_list)

@app.route('/counter/view/<branch>/<cust_type>/<counter_no>', methods=['GET'])
def counter_call(branch, cust_type, counter_no): 
    next_queue = ""
    file_data = utils.extract_data(branch, queue)
    missed_queue_list = utils.get_missed_queue_list(file_data, cust_type)
    call_type = request.args.get('call_type')
    try:
        if call_type == 'call':
            next_queue = utils.call_queue(branch, file_data, cust_type)
            queue_list[branch]={counter_no:next_queue}
        elif call_type == 'next':
           utils.clear_current_queue(branch, file_data, cust_type)
           next_queue = utils.call_queue(branch, file_data, cust_type)
           queue_list[branch]={counter_no:next_queue}
        elif call_type == 'hold':
           missed_queue = utils.call_queue(branch, file_data, cust_type)
           utils.missed_queue(branch, file_data, cust_type, missed_queue)
           next_queue = f" {missed_queue} missed"
        elif call_type == 'reschedule':
           requeue_no = request.args.get('requeue_no')
           utils.requeue(branch, file_data, cust_type, requeue_no)
           next_queue = f" {requeue_no} rescheduled"
    except:
        next_queue = 'No more queue'
    
    if next_queue is None:
        next_queue = 'No more queue'
    
    cust_type = cust_type.capitalize() + ' Banking'
    
    return render_template('CounterView.html', branch = branch, 
                                                cust_type = cust_type,
                                                counter_no = counter_no,
                                                next_queue = next_queue,
                                                missed_queue_list = missed_queue_list)


################## Display ##################
@app.route('/display', methods=['GET'])
def display_main():
    return render_template('Display.html', branches_list = branches_list)
    
@app.route('/display/', methods=['GET'])
def display_main2():
    return render_template('Display.html', branches_list = branches_list)

@app.route('/display/<branch>', methods=['GET'])
def display_branch(branch):
    if len(queue_list[branch])==0:
        counter_no = 'no queue'
        queue_no = "no queue"
    else:
        for key,value in queue_list[branch].items():
            counter_no=key
            queue_no = value
        
    file_data = utils.extract_data(branch, queue)
    priority_q = utils.display_three(file_data, 'priority')
    personal_q = utils.display_three(file_data, 'personal')
    corporate_q = utils.display_three(file_data, 'corporate')
    priority_q = ' '.join(priority_q)
    personal_q = ' '.join(personal_q)
    corporate_q = ' '.join(corporate_q)
        
    return render_template('Display.html', branches_list = branches_list, 
                                           counter_no = counter_no,
                                           queue_no = queue_no,
                                           priority_q = priority_q,
                                           personal_q = personal_q,
                                           corporate_q = corporate_q)
if __name__ == "__main__":
    app.run(port=3000)