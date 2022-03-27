#!/usr/bin/env python3

from kubernetes import client, config, watch
from skpy import Skype

skype = Skype('kubernetes@mdminhazulhaque.io', 'Miech0aishaing8I')
kubernetes_alert = '12:a776ef0e4ca14312b6364395462d10e8@thread.skype'

config.load_kube_config()

v1 = client.CoreV1Api()
w = watch.Watch()

for event in w.stream(v1.list_event_for_all_namespaces, field_selector="type!=Normal"):
  namespace = event['raw_object']['metadata']['namespace']
  involvedObject = event['raw_object']['involvedObject']['name']
  message = event['raw_object']['message']
  button = None
  if "production" in namespace:
    button = '(redcircle)'
  else:
    button = '(yellowcircle)'
  
  line = F"{button} {namespace}\n(gear) {involvedObject}\n(scroll) {message}"
  skype.chats[kubernetes_alert].sendMsg(line)
