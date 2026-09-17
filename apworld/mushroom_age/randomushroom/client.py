class RandoClient:
    def __init__(self, game_manager, tcp_client_socket):
        self.game_manager = game_manager
        self.tcp_client_socket = tcp_client_socket


    # signals received from game
    def on_begin_task(self, chapter, task_id):
        task = LOCATION_NAME_STRING.format(chapter + 1, task_id + 1)

        if self.game_manager.check_if_task_available(task):
            items = self.game_manager.check_task_gates(task)
            self.send_gate(items)
    
    def on_task_complete(self, chapter, task_id):
        task = LOCATION_NAME_STRING.format(chapter + 1, task_id + 1)

        if self.game_manager.complete_task(task):
            self.send_check(task)

    def on_object_collected(self, chapter, task_id, object_id): 
        task = LOCATION_NAME_STRING_BONUS.format(chapter + 1, task_id + 1)

        if self.game_manager.collect_task_item(task, object_id):
            self.send_check(f"task")

    # signals sent to game
    def send_gate(self, items):
        self.send_payload("rand_main_menu", [])
        self.send_payload("rand_display_text", [f"You cannot play that task right now!\nYou need: {items}"]) # TODO: test and improve

    def send_item_notification(self, item):
        self.send_payload("rand_display_text", [f"You received {item}!"]) # TODO: test and improve


    # signals received from AP
    def on_receive_check(self, check): # TODO: receive from AP
        ... # TODO: convert signal into self.receive_item call

    # signals sent to AP
    def send_check(self, check):
        ... # TODO: send signal to AP


    # helper functions
    def receive_item(self, item):
        if self.game_manager.receive_item(item):
            self.send_item_notification(item)
