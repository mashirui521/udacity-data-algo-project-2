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

    # Test case 1: user is directly in the group -> Return True
    # Test case 2: user is in the subgroup       -> Return True
    # Test case 3: user is not in the group      -> Return False
    # Test case 4: invalid user name             -> Return False
    # Test case 5: invalid group                 -> Return False

    # tuple: (user, group, expected return)
    test_data = [('Visitor1', group_external, True),    \
                 ('Tom',      group_company,  True),    \
                 ('Peter',    group_worker,   False),   \
                 (123,        group_manager,  False),   \
                 ('Peter',    None,           False)]

    for i, (user, group, target_result) in enumerate(test_data, 1):
        if is_user_in_group(user, group) == target_result:
            print('Test case {}: Pass'.format(i))
        else:
            print('Test case {}: Failed'.format(i))

test()