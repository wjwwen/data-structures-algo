import json
import os 

queue_type = {'priority':0,'personal':1,'corporate':2}

# Writing branch file for queue
def write_file(branch, data):
    fileName = f'./data/{branch}' + '.json'
    ## Initiate queues by creating json 
    with open(fileName, "w") as fp:
        json.dump(data, fp, indent=4) 

        
# Loading branch queues 
def load(branch):
    fileName = fileName = f'./data/{branch}' + '.json'
    with open(fileName) as user_file:
        parsed_json = json.load(user_file)
        return (parsed_json)

# Check if branch data exists 
def extract_data(branch, data):
    try: 
        file_data = load(branch)
    except:
        write_file(branch, data)
        file_data = load(branch)
    return file_data

# Addin q for customer
def addNewqueue(data, cust_type, branch):
        #to check if branch is still available for queue collection
    if data[queue_type[cust_type]]['pause_queue'] is True:
        message = 'Please come back again later'
    # To generate new queue number using branch code and counter
    else:
        data[queue_type[cust_type]]['counter']+=1
        queue_no = branch[0] + str(data[queue_type[cust_type]]['counter']+(queue_type[cust_type]+1)*1000)
        data[queue_type[cust_type]]['queue'].append(queue_no)
        message = f"Your queue number is {queue_no} for branch {branch} for {cust_type.capitalize()} banking!"
    write_file(branch, data)
    return message


# Display queue message for CRO 
def display_q_message(cust_type, data):
    if data[queue_type[cust_type]]["pause_queue"] == False:
        hold_queue = 'Initiated'
    else:
        hold_queue = 'Paused'
    
    message = f'{hold_queue}: {len(data[queue_type[cust_type]]["queue"])} waiting'
    return message

# Clearning q for CRO 
def clear_queue(branch):
    try: 
        path = os.path.join(os.getcwd() + '\data')
        os.remove(os.path.join(path + '\\' + branch + '.json'))
    except:
        pass
    q_clear_notif = 'Queues cleared'
    return q_clear_notif


def get_missed_queue_list(data, cust_type):
    return data[queue_type[cust_type]]["hold_queue"]

def call_queue(branch, data, cust_type):
    #to check if branch is still available for queue collection
    if len(data[queue_type[cust_type]]['hold_queue']) == 0 and len(data[queue_type[cust_type]]['queue']) == 0:
        pass
    elif len(data[queue_type[cust_type]]['queue']) == 0 and len(data[queue_type[cust_type]]['hold_queue']) > 0:
        return data[queue_type[cust_type]]['hold_queue'][0]
    # To generate new queue number using branch code and counter
    else:
        return data[queue_type[cust_type]]['queue'][0]

def clear_current_queue(branch, data, cust_type):
        #to check if branch is still available for queue collection
        if len(data[queue_type[cust_type]]['queue']) == 0:
            pass
        else:
            data[queue_type[cust_type]]["queue"].remove(data[queue_type[cust_type]]["queue"][0])
            write_file(branch, data)
      

def missed_queue(branch, data, cust_type, queue_no):
    # To remove queue number from main queue
    data[queue_type[cust_type]]['queue'].remove(queue_no)
    # To add queue number to missed queue list
    data[queue_type[cust_type]]['hold_queue'].append(queue_no)
    write_file(branch, data)


def requeue(branch, data, cust_type, queue_no):
    # To remove queue number from hold_queue
    data[queue_type[cust_type]]["hold_queue"].remove(queue_no)
    data[queue_type[cust_type]]['queue'].insert(2, queue_no)
    write_file(branch, data)
    
def display_three(data, cust_type):
    last_three = data[queue_type[cust_type]]["queue"][1:4]
    return last_three
    
    

if __name__ == "__main__":
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
    write_file('Yishun', queue)
    q = load('Yishun')
    
    addNewqueue('Yishun', 'priority')
    addNewqueue('Yishun', 'priority')
    addNewqueue('Yishun', 'corporate')
    addNewqueue('Yishun', 'priority')
    addNewqueue('Yishun', 'priority')
    addNewqueue('Yishun', 'corporate')
    addNewqueue('Yishun', 'personal')
    print(call_queue('Yishun', 'personal'))
    print(call_queue('Yishun', 'priority'))
    # clear_current_queue('Yishun', 'priority')
    # stopstart_queue('Yishun', 'personal',"stop")
    # addNewqueue('Yishun', 'personal')
    # missed_queue('Yishun', 'priority',"Y1001")
    # requeue('Yishun', 'priority',"Y1001")
    # stopstart_queue('Yishun', 'personal',"start")
    # addNewqueue('Yishun', 'personal')
    print(q[0]['queue'])
    print(len(q))



