class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def breath_first_search(user, group, queue):
    if group:
        queue += group.get_groups()
        if user in group.get_users():
            return True
        else:
            if len(queue) != 0:
                return breath_first_search(user, queue.pop(0), queue)
    return False

def is_user_in_group(user, group):
    queue = list()
    return breath_first_search(user, group, queue)

###################################  TEST  ###############################################
def test():
    group_company = Group('company')
    group_internal = Group('internal')
    group_external = Group('external')
    group_admin = Group('admin')
    group_manager = Group('manager')
    group_worker = Group('worker')

    group_worker.add_user('Tom')
    group_worker.add_user('Thomas')
    group_worker.add_user('Luis')

    group_manager.add_user('Stefan')
    
    group_admin.add_user('Peter')

    group_external.add_user('Visitor1')

    group_company.add_group(group_internal)
    group_company.add_group(group_external)
    group_internal.add_group(group_admin)
    group_internal.add_group(group_manager)
    group_internal.add_group(group_worker)

    test_data = [('Visitor1', group_external, True),   \
                 ('Tom',      group_company,  True),   \
                 ('Stefan',   group_manager,  True),   \
                 ('Peter',    group_worker,   False)]

    for user, group, target_result in test_data:
        if is_user_in_group(user, group) == target_result:
            print('Pass')
        else:
            print('Failed')

test()