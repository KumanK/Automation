from epo_login import login
import system_tree
import actions
import time

obj = login()
driver = obj.load_home_page("https://192.168.1.13:8443/")
tree = system_tree.systemTree(driver)
tree.go_to_system_tree()
tree.select_group("This Group and All Subgroups")
tree.quick_find("bcm-")
tree.select_system()
time.sleep(2)
act = actions.actions(driver)
# act.click_on_Actions()
act.select_agent_and_click___Run_Client_Task_Now()
act.run_solidcore_client_task(name="SC: Disable")
