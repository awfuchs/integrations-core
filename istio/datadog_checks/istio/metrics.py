# (C) Datadog, Inc. 2020 - Present
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)


GENERIC_METRICS = {
    'go_gc_duration_seconds': 'go.gc_duration_seconds',
    'go_goroutines': 'go.goroutines',
    'go_info': 'go.info',
    'go_memstats_alloc_bytes': 'go.memstats.alloc_bytes',
    'go_memstats_alloc_bytes_total': 'go.memstats.alloc_bytes_total',
    'go_memstats_buck_hash_sys_bytes': 'go.memstats.buck_hash_sys_bytes',
    'go_memstats_frees_total': 'go.memstats.frees_total',
    'go_memstats_gc_cpu_fraction': 'go.memstats.gc_cpu_fraction',
    'go_memstats_gc_sys_bytes': 'go.memstats.gc_sys_bytes',
    'go_memstats_heap_alloc_bytes': 'go.memstats.heap_alloc_bytes',
    'go_memstats_heap_idle_bytes': 'go.memstats.heap_idle_bytes',
    'go_memstats_heap_inuse_bytes': 'go.memstats.heap_inuse_bytes',
    'go_memstats_heap_objects': 'go.memstats.heap_objects',
    'go_memstats_heap_released_bytes': 'go.memstats.heap_released_bytes',
    'go_memstats_heap_sys_bytes': 'go.memstats.heap_sys_bytes',
    'go_memstats_last_gc_time_seconds': 'go.memstats.last_gc_time_seconds',
    'go_memstats_lookups_total': 'go.memstats.lookups_total',
    'go_memstats_mallocs_total': 'go.memstats.mallocs_total',
    'go_memstats_mcache_inuse_bytes': 'go.memstats.mcache_inuse_bytes',
    'go_memstats_mcache_sys_bytes': 'go.memstats.mcache_sys_bytes',
    'go_memstats_mspan_inuse_bytes': 'go.memstats.mspan_inuse_bytes',
    'go_memstats_mspan_sys_bytes': 'go.memstats.mspan_sys_bytes',
    'go_memstats_next_gc_bytes': 'go.memstats.next_gc_bytes',
    'go_memstats_other_sys_bytes': 'go.memstats.other_sys_bytes',
    'go_memstats_stack_inuse_bytes': 'go.memstats.stack_inuse_bytes',
    'go_memstats_stack_sys_bytes': 'go.memstats.stack_sys_bytes',
    'go_memstats_sys_bytes': 'go.memstats.sys_bytes',
    'go_threads': 'go.threads',
    'process_cpu_seconds_total': 'process.cpu_seconds_total',
    'process_max_fds': 'process.max_fds',
    'process_open_fds': 'process.open_fds',
    'process_resident_memory_bytes': 'process.resident_memory_bytes',
    'process_start_time_seconds': 'process.start_time_seconds',
    'process_virtual_memory_bytes': 'process.virtual_memory_bytes',
}


CITADEL_METRICS = {
    'citadel_secret_controller_csr_err_count': 'secret_controller.csr_err_count',
    'citadel_secret_controller_secret_deleted_cert_count': ('secret_controller.secret_deleted_cert_count'),
    'citadel_secret_controller_svc_acc_created_cert_count': ('secret_controller.svc_acc_created_cert_count'),
    'citadel_secret_controller_svc_acc_deleted_cert_count': ('secret_controller.svc_acc_deleted_cert_count'),
    'citadel_server_authentication_failure_count': 'server.authentication_failure_count',
    'citadel_server_citadel_root_cert_expiry_timestamp': ('server.citadel_root_cert_expiry_timestamp'),
    'citadel_server_csr_count': 'server.csr_count',
    'citadel_server_csr_parsing_err_count': 'server.csr_parsing_err_count',
    'citadel_server_id_extraction_err_count': 'server.id_extraction_err_count',
    'citadel_server_success_cert_issuance_count': 'server.success_cert_issuance_count',
    'citadel_server_root_cert_expiry_timestamp': 'server.root_cert_expiry_timestamp',
}


GALLEY_METRICS = {
    'endpoint_no_pod': 'endpoint_no_pod',
    'galley_mcp_source_clients_total': 'mcp_source.clients_total',
    'galley_runtime_processor_event_span_duration_milliseconds': ('runtime_processor.event_span_duration_milliseconds'),
    'galley_runtime_processor_events_processed_total': 'runtime_processor.events_processed_total',
    'galley_runtime_processor_snapshot_events_total': 'runtime_processor.snapshot_events_total',
    'galley_runtime_processor_snapshot_lifetime_duration_milliseconds': (
        'runtime_processor.snapshot_lifetime_duration_milliseconds'
    ),
    'galley_runtime_processor_snapshots_published_total': ('runtime_processor.snapshots_published_total'),
    'galley_runtime_state_type_instances_total': 'runtime_state_type_instances_total',
    'galley_runtime_strategy_on_change_total': 'runtime_strategy.on_change_total',
    'galley_runtime_strategy_timer_max_time_reached_total': ('runtime_strategy.timer_max_time_reached_total'),
    'galley_runtime_strategy_timer_quiesce_reached_total': 'runtime_strategy.quiesce_reached_total',
    'galley_runtime_strategy_timer_resets_total': 'runtime_strategy.timer_resets_total',
    'galley_source_kube_dynamic_converter_success_total': ('source_kube.dynamic_converter_success_total'),
    'galley_source_kube_event_success_total': 'source_kube.event_success_total',
    'galley_validation_cert_key_updates': 'validation.cert_key_updates',
    'galley_validation_config_load': 'validation.config_load',
    'galley_validation_config_updates': 'validation.config_update',
    'galley_validation_passed': 'validation.passed',
    # These metrics supported Istio 1.5
    'galley_validation_config_update_error': 'validation.config_update_error',
    'galley_source_kube_event_error_total': 'galley.source.kube.event.error',
    'galley_source_kube_dynamic_converter_failure_total': 'galley.source.kube.dynamic.converter.failure',
    'galley_validation_cert_key_update_errors': 'galley.validation.cert.key.update.errors',
    'galley_validation_http_error': 'galley.validation.http.error',
}


MESH_METRICS = {
    'istio_request_messages_total': 'request.messages.total',
    'istio_response_messages_total': 'response.messages.total',
    # These metrics support Istio 1.5
    'istio_request_duration_milliseconds': 'request.duration.milliseconds',
    # These metrics support Istio 1.0
    'istio_requests_total': 'request.count',
    'istio_request_duration_seconds': 'request.duration',
    'istio_request_bytes': 'request.size',
    'istio_response_bytes': 'response.size',
    # These metrics support Istio 0.8
    'istio_request_count': 'request.count',
    'istio_request_duration': 'request.duration',
    'istio_request_size': 'request.size',
    'istio_response_size': 'response.size',
    # TCP metrics
    'istio_tcp_connections_closed_total': 'tcp.connections_closed.total',
    'istio_tcp_connections_opened_total': 'tcp.connections_opened.total',
    'istio_tcp_received_bytes_total': 'tcp.received_bytes.total',
    'istio_tcp_sent_bytes_total': 'tcp.send_bytes.total',
    'istio_agent_pilot_conflict_outbound_listener_http_over_current_tcp': (
        'agent.pilot.conflict.outbound_listener.http_over_current_tcp'
    ),
    'istio_agent_go_memstats_stack_sys_bytes': 'agent.go.memstats.stack_sys_bytes',
    'istio_agent_pilot_conflict_inbound_listener': 'agent.conflict.inbound_listener',
    'istio_agent_go_memstats_sys_bytes': 'agent.go.memstats.sys_bytes',
    'istio_agent_pilot_xds': 'agent.pilot.xds',
    'istio_agent_go_memstats_alloc_bytes': 'agent.go.memstats.alloc_bytes',
    'istio_agent_go_memstats_heap_idle_bytes': 'agent.go.memstats.heap_idle_bytes',
    'istio_agent_process_resident_memory_bytes': 'agent.process.resident_memory_bytes',
    'istio_agent_go_memstats_alloc_bytes_total': 'agent.go.memstats.alloc_bytes_total',
    'istio_agent_pilot_conflict_outbound_listener_tcp_over_current_tcp': (
        'agent.conflict.outbound_listener.tcp_over_current_tcp'
    ),
    'istio_agent_go_memstats_gc_cpu_fraction': 'agent.go.memstats.gc_cpu_fraction',
    'istio_agent_go_memstats_heap_sys_bytes': 'agent.go.memstats.heap_sys_bytes',
    'istio_agent_go_memstats_stack_inuse_bytes': 'agent.go.memstats.stack_inuse_bytes',
    'istio_agent_go_memstats_heap_released_bytes': 'agent.go.memstats.heap_released_bytes',
    'istio_agent_go_memstats_mspan_inuse_bytes': 'agent.go.memstats.mspan_inuse_bytes',
    'istio_agent_go_memstats_mallocs_total': 'agent.go.memstats.mallocs_total',
    'istio_agent_pilot_endpoint_not_ready': 'agent.pilot.endpoint_not_ready',
    'istio_agent_pilot_no_ip': 'agent.pilot.no_ip',
    'istio_agent_num_outgoing_requests': 'agent.num_outgoing_requests',
    'istio_agent_go_memstats_other_sys_bytes': 'agent.go.memstats.other_sys_bytes',
    'istio_agent_pilot_xds_config_size_bytes': 'agent.pilot.xds.config_size_bytes',
    'istio_agent_process_open_fds': 'agent.process.open_fds',
    'istio_agent_go_goroutines': 'agent.go.goroutines',
    'istio_agent_go_threads': 'agent.go.threads',
    'istio_agent_go_info': 'agent.go.info',
    'istio_agent_go_memstats_frees_total': 'agent.go.memstats.frees_total',
    'istio_agent_go_memstats_mcache_inuse_bytes': 'agent.go.memstats.mcache_inuse_bytes',
    'istio_agent_process_virtual_memory_bytes': 'agent.process.virtual_memory_bytes',
    'istio_agent_endpoint_no_pod': 'agent.endpoint_no_pod',
    'istio_agent_go_gc_duration_seconds': 'agent.go.gc_duration_seconds',
    'istio_agent_process_cpu_seconds_total': 'agent.process.cpu_seconds_total',
    'istio_agent_go_memstats_heap_objects': 'agent.go.memstats.heap_objects',
    'istio_agent_pilot_vservice_dup_domain': 'agent.pilot.vservice_dup_domain',
    'istio_agent_process_virtual_memory_max_bytes': 'agent.process.virtual_memory_max_bytes',
    'istio_agent_go_memstats_mcache_sys_bytes': 'agent.go.memstats.mcache_sys_bytes',
    'istio_agent_scrapes_total': 'agent.scrapes_total',
    'istio_agent_pilot_duplicate_envoy_clusters': 'agent.pilot.duplicate_envoy_clusters',
    'istio_agent_go_memstats_buck_hash_sys_bytes': 'agent.go.memstats.buck_hash_sys_bytes',
    'istio_agent_pilot_xds_push_time': 'agent.pilot.xds.push_time',
    'istio_agent_wasm_cache_entries': 'agent.wasm_cache_entries',
    'istio_agent_pilot_eds_no_instances': 'agent.pilot.eds_no_instances',
    'istio_agent_go_memstats_heap_alloc_bytes': 'agent.go.memstats.heap_alloc_bytes',
    'istio_agent_pilot_virt_services': 'agent.pilot.virt_services',
    'istio_agent_go_memstats_next_gc_bytes': 'agent.go.memstats.next_gc_bytes',
    'istio_agent_startup_duration_seconds': 'agent.startup_duration_seconds',
    'istio_agent_go_memstats_last_gc_time_seconds': 'agent.go.memstats.last_gc_time_seconds',
    'istio_agent_pilot_xds_send_time': 'agent.pilot.xds.send_time',
    'istio_agent_go_memstats_heap_inuse_bytes': 'agent.go.memstats.heap_inuse_bytes',
    'istio_agent_process_max_fds': 'agent.process.max_fds',
    'istio_agent_go_memstats_gc_sys_bytes': 'agent.go.memstats.gc_sys_bytes',
    'istio_agent_pilot_destrule_subsets': 'agent.pilot.destrule_subsets',
    'istio_agent_pilot_xds_pushes': 'agent.pilot.xds.pushes',
    'istio_agent_process_start_time_seconds': 'agent.process.start_time_seconds',
    'istio_agent_go_memstats_lookups_total': 'agent.go.memstats.lookups_total',
    'istio_agent_outgoing_latency': 'agent.outgoing_latency',
    'istio_agent_go_memstats_mspan_sys_bytes': 'agent.go.memstats.mspan_sys_bytes',
    'istio_agent_pilot_conflict_outbound_listener_tcp_over_current_http': (
        'agent.pilot.conflict.outbound_listener.tcp_over_current_http'
    ),
}


MIXER_METRICS = {
    # Pre 1.1 metrics
    'grpc_server_handled_total': 'grpc.server.handled_total',
    'grpc_server_handling_seconds': 'grpc.server.handling_seconds',
    'grpc_server_msg_received_total': 'grpc.server.msg_received_total',
    'grpc_server_msg_sent_total': 'grpc.server.msg_sent_total',
    'grpc_server_started_total': 'grpc.server.started_total',
    'mixer_adapter_dispatch_count': 'adapter.dispatch_count',
    'mixer_adapter_dispatch_duration': 'adapter.dispatch_duration',
    'mixer_adapter_old_dispatch_count': 'adapter.old_dispatch_count',
    'mixer_adapter_old_dispatch_duration': 'adapter.old_dispatch_duration',
    'mixer_config_resolve_actions': 'config.resolve_actions',
    'mixer_config_resolve_count': 'config.resolve_count',
    'mixer_config_resolve_duration': 'config.resolve_duration',
    'mixer_config_resolve_rules': 'config.resolve_rules',
    # 1.1 metrics
    'grpc_io_server_completed_rpcs': 'grpc_io_server.completed_rpcs',
    'grpc_io_server_received_bytes_per_rpc': 'grpc_io_server.received_bytes_per_rpc',
    'grpc_io_server_sent_bytes_per_rpc': 'grpc_io_server.sent_bytes_per_rpc',
    'grpc_io_server_server_latency': 'grpc_io_server.server_latency',
    'mixer_config_attributes_total': 'config.attributes_total',
    'mixer_config_handler_configs_total': 'config.handler_configs_total',
    'mixer_config_instance_configs_total': 'config.instance_configs_total',
    'mixer_config_rule_configs_total': 'config.rule_configs_total',
    'mixer_dispatcher_destinations_per_request': 'dispatcher.destinations_per_request',
    'mixer_dispatcher_instances_per_request': 'dispatcher.instances_per_request',
    'mixer_handler_daemons_total': 'handler.daemons',
    'mixer_handler_new_handlers_total': 'handler.new_handlers_total',
    'mixer_mcp_sink_reconnections': 'mcp_sink.reconnections',
    'mixer_mcp_sink_request_acks_total': 'mcp_sink.request_acks_total',
    'mixer_runtime_dispatches_total': 'runtime.dispatches_total',
    'mixer_runtime_dispatch_duration_seconds': 'runtime.dispatch_duration_seconds',
    'mixer_config_rule_config_errors_total': 'config.rule.config.errors_total',
    'mixer_config_rule_config_match_error_total': 'config.rule.config.match.errors_total',
    'mixer_config_unsatisfied_action_handler_total': 'config.unsatisfied.action.handlers_total',
    'mixer_config_adapter_info_config_errors_total': 'config.adapter.info.config.errors_total',
    'mixer_config_handler_validation_error_total': 'config.handler.validation.errors_total',
    'mixer_config_instance_config_errors_total': 'config.instance.config.errors_total',
    'mixer_handler_handler_build_failures_total': 'handler.handler.build.failures_total',
    'mixer_config_adapter_info_configs_total': 'config.adapter.info.configs_total',
    # These don't have much documentation around them aside from being mentioned once
    'mixer_config_rule_config_error_count': 'config.rule.config.errors',
    'mixer_config_rule_config_match_error_count': 'config.rule.config.match.errors',
    'mixer_config_unsatisfied_action_handler_count': 'config.unsatisfied.action.handlers',
    'mixer_config_adapter_info_config_error_count': 'config.adapter.info.config.errors',
    'mixer_config_handler_validation_error_count': 'config.handler.validation.errors',
    'mixer_config_instance_config_error_count': 'config.instance.config.errors',
    'mixer_handler_handler_build_failure_count': 'handler.handler.build.failures',
}

PILOT_METRICS = {
    'pilot_conflict_inbound_listener': 'conflict.inbound_listener',
    'pilot_conflict_outbound_listener_http_over_current_tcp': ('conflict.outbound_listener.http_over_current_tcp'),
    'pilot_conflict_outbound_listener_tcp_over_current_http': ('conflict.outbound_listener.tcp_over_current_http'),
    'pilot_conflict_outbound_listener_tcp_over_current_tcp': ('conflict.outbound_listener.tcp_over_current_tcp'),
    'pilot_destrule_subsets': 'destrule_subsets',
    'pilot_duplicate_envoy_clusters': 'duplicate_envoy_clusters',
    'pilot_eds_no_instances': 'eds_no_instances',
    'pilot_endpoint_not_ready': 'endpoint_not_ready',
    'pilot_invalid_out_listeners': 'invalid_out_listeners',
    'pilot_mcp_sink_reconnections': 'mcp_sink.reconnections',
    'pilot_mcp_sink_recv_failures_total': 'mcp_sink.recv_failures_total',
    'pilot_mcp_sink_request_acks_total': 'mcp_sink.request_acks_total',
    'pilot_no_ip': 'no_ip',
    'pilot_proxy_convergence_time': 'proxy_convergence_time',
    'pilot_rds_expired_nonce': 'rds_expired_nonce',
    'pilot_services': 'services',
    'pilot_total_xds_internal_errors': 'total_xds_internal_errors',
    'pilot_total_xds_rejects': 'total_xds_rejects',
    'pilot_virt_services': 'virt_services',
    'pilot_vservice_dup_domain': 'vservice_dup_domain',
    'pilot_xds': 'xds',
    'pilot_xds_eds_instances': 'xds.eds_instances',
    'pilot_xds_push_context_errors': 'xds.push.context_errors',
    'pilot_xds_push_timeout': 'xds.push.timeout',
    'pilot_xds_push_timeout_failures': 'xds.push.timeout_failures',
    'pilot_xds_pushes': 'xds.pushes',
    'pilot_xds_write_timeout': 'xds.write_timeout',
    'pilot_xds_rds_reject': 'pilot.xds.rds_reject',
    'pilot_xds_eds_reject': 'pilot.xds.eds_reject',
    'pilot_xds_cds_reject': 'pilot.xds.cds_reject',
    'pilot_xds_lds_reject': 'pilot.xds.lds_reject',
}


ISTIOD_METRICS = {
    # Maintain namespace compatibility from legacy components
    # Generic metrics
    'go_gc_duration_seconds': 'go.gc_duration_seconds',
    'go_goroutines': 'go.goroutines',
    'go_info': 'go.info',
    'go_memstats_alloc_bytes': 'go.memstats.alloc_bytes',
    'go_memstats_alloc_bytes_total': 'go.memstats.alloc_bytes_total',
    'go_memstats_buck_hash_sys_bytes': 'go.memstats.buck_hash_sys_bytes',
    'go_memstats_frees_total': 'go.memstats.frees_total',
    'go_memstats_gc_cpu_fraction': 'go.memstats.gc_cpu_fraction',
    'go_memstats_gc_sys_bytes': 'go.memstats.gc_sys_bytes',
    'go_memstats_heap_alloc_bytes': 'go.memstats.heap_alloc_bytes',
    'go_memstats_heap_idle_bytes': 'go.memstats.heap_idle_bytes',
    'go_memstats_heap_inuse_bytes': 'go.memstats.heap_inuse_bytes',
    'go_memstats_heap_objects': 'go.memstats.heap_objects',
    'go_memstats_heap_released_bytes': 'go.memstats.heap_released_bytes',
    'go_memstats_heap_sys_bytes': 'go.memstats.heap_sys_bytes',
    'go_memstats_last_gc_time_seconds': 'go.memstats.last_gc_time_seconds',
    'go_memstats_lookups_total': 'go.memstats.lookups_total',
    'go_memstats_mallocs_total': 'go.memstats.mallocs_total',
    'go_memstats_mcache_inuse_bytes': 'go.memstats.mcache_inuse_bytes',
    'go_memstats_mcache_sys_bytes': 'go.memstats.mcache_sys_bytes',
    'go_memstats_mspan_inuse_bytes': 'go.memstats.mspan_inuse_bytes',
    'go_memstats_mspan_sys_bytes': 'go.memstats.mspan_sys_bytes',
    'go_memstats_next_gc_bytes': 'go.memstats.next_gc_bytes',
    'go_memstats_other_sys_bytes': 'go.memstats.other_sys_bytes',
    'go_memstats_stack_inuse_bytes': 'go.memstats.stack_inuse_bytes',
    'go_memstats_stack_sys_bytes': 'go.memstats.stack_sys_bytes',
    'go_memstats_sys_bytes': 'go.memstats.sys_bytes',
    'go_threads': 'go.threads',
    'process_cpu_seconds_total': 'process.cpu_seconds_total',
    'process_max_fds': 'process.max_fds',
    'process_open_fds': 'process.open_fds',
    'process_resident_memory_bytes': 'process.resident_memory_bytes',
    'process_start_time_seconds': 'process.start_time_seconds',
    'process_virtual_memory_bytes': 'process.virtual_memory_bytes',
    'pilot_conflict_inbound_listener': 'pilot.conflict.inbound_listener',
    'pilot_conflict_outbound_listener_http_over_current_tcp': (
        'pilot.conflict.outbound_listener.http_over_current_tcp'
    ),
    'pilot_conflict_outbound_listener_tcp_over_current_http': (
        'pilot.conflict.outbound_listener.tcp_over_current_http'
    ),
    'pilot_conflict_outbound_listener_tcp_over_current_tcp': ('pilot.conflict.outbound_listener.tcp_over_current_tcp'),
    'pilot_destrule_subsets': 'pilot.destrule_subsets',
    'pilot_duplicate_envoy_clusters': 'pilot.duplicate_envoy_clusters',
    'pilot_eds_no_instances': 'pilot.eds_no_instances',
    'pilot_endpoint_not_ready': 'pilot.endpoint_not_ready',
    'pilot_invalid_out_listeners': 'pilot.invalid_out_listeners',
    'pilot_mcp_sink_reconnections': 'pilot.mcp_sink.reconnections',
    'pilot_mcp_sink_recv_failures_total': 'pilot.mcp_sink.recv_failures_total',
    'pilot_mcp_sink_request_acks_total': 'pilot.mcp_sink.request_acks_total',
    'pilot_no_ip': 'pilot.no_ip',
    'pilot_proxy_convergence_time': 'pilot.proxy_convergence_time',
    'pilot_rds_expired_nonce': 'pilot.rds_expired_nonce',
    'pilot_services': 'pilot.services',
    'pilot_total_xds_internal_errors': 'pilot.total_xds_internal_errors',
    'pilot_total_xds_rejects': 'pilot.total_xds_rejects',
    'pilot_virt_services': 'pilot.virt_services',
    'pilot_vservice_dup_domain': 'pilot.vservice_dup_domain',
    'pilot_xds': 'pilot.xds',
    'pilot_xds_eds_instances': 'pilot.xds.eds_instances',
    'pilot_xds_push_context_errors': 'pilot.xds.push.context_errors',
    'pilot_xds_push_timeout': 'pilot.xds.push.timeout',
    'pilot_xds_push_timeout_failures': 'pilot.xds.push.timeout_failures',
    'pilot_xds_pushes': 'pilot.xds.pushes',
    'pilot_xds_write_timeout': 'pilot.xds.write_timeout',
    'pilot_xds_rds_reject': 'pilot.xds.rds_reject',
    'pilot_xds_eds_reject': 'pilot.xds.eds_reject',
    'pilot_xds_cds_reject': 'pilot.xds.cds_reject',
    'pilot_xds_lds_reject': 'pilot.xds.lds_reject',
    'grpc_server_handled_total': 'grpc.server.handled_total',
    'grpc_server_handling_seconds': 'grpc.server.handling_seconds',
    'grpc_server_msg_received_total': 'grpc.server.msg_received_total',
    'grpc_server_msg_sent_total': 'grpc.server.msg_sent_total',
    'grpc_server_started_total': 'grpc.server.started_total',
    'grpc_io_server_completed_rpcs': 'mixer.grpc_io_server.completed_rpcs',
    'grpc_io_server_received_bytes_per_rpc': 'mixer.grpc_io_server.received_bytes_per_rpc',
    'grpc_io_server_sent_bytes_per_rpc': 'mixer.grpc_io_server.sent_bytes_per_rpc',
    'grpc_io_server_server_latency': 'mixer.grpc_io_server.server_latency',
    'mixer_config_attributes_total': 'mixer.config.attributes_total',
    'mixer_config_handler_configs_total': 'mixer.config.handler_configs_total',
    'mixer_config_instance_configs_total': 'mixer.config.instance_configs_total',
    'mixer_config_rule_configs_total': 'mixer.config.rule_configs_total',
    'mixer_dispatcher_destinations_per_request': 'mixer.dispatcher.destinations_per_request',
    'mixer_dispatcher_instances_per_request': 'mixer.dispatcher.instances_per_request',
    'mixer_handler_daemons_total': 'mixer.handler.daemons_total',
    'mixer_handler_new_handlers_total': 'mixer.handler.new_handlers_total',
    'mixer_mcp_sink_reconnections': 'mixer.mcp_sink.reconnections',
    'mixer_mcp_sink_request_acks_total': 'mixer.mcp_sink.request_acks_total',
    'mixer_runtime_dispatches_total': 'mixer.runtime.dispatches_total',
    'mixer_runtime_dispatch_duration_seconds': 'mixer.runtime.dispatch_duration_seconds',
    'endpoint_no_pod': 'galley.endpoint_no_pod',
    'galley_mcp_source_clients_total': 'galley.mcp_source.clients_total',
    'galley_runtime_processor_event_span_duration_milliseconds': (
        'galley.runtime_processor.event_span_duration_milliseconds'
    ),
    'galley_runtime_processor_events_processed_total': 'galley.runtime_processor.events_processed_total',
    'galley_runtime_processor_snapshot_events_total': 'galley.runtime_processor.snapshot_events_total',
    'galley_runtime_processor_snapshot_lifetime_duration_milliseconds': (
        'galley.runtime_processor.snapshot_lifetime_duration_milliseconds'
    ),
    'galley_runtime_processor_snapshots_published_total': ('galley.runtime_processor.snapshots_published_total'),
    'galley_runtime_state_type_instances_total': 'galley.runtime_state_type_instances_total',
    'galley_runtime_strategy_on_change_total': 'galley.runtime_strategy.on_change_total',
    'galley_runtime_strategy_timer_max_time_reached_total': ('galley.runtime_strategy.timer_max_time_reached_total'),
    'galley_runtime_strategy_timer_quiesce_reached_total': 'galley.runtime_strategy.quiesce_reached_total',
    'galley_runtime_strategy_timer_resets_total': 'galley.runtime_strategy.timer_resets_total',
    'galley_source_kube_dynamic_converter_success_total': ('galley.source_kube.dynamic_converter_success_total'),
    'galley_source_kube_event_success_total': 'galley.source_kube.event_success_total',
    'galley_validation_config_load': 'galley.validation.config_load',
    'galley_validation_config_updates': 'galley.validation.config_update',
    'citadel_secret_controller_csr_err_count': 'citadel.secret_controller.csr_err_count',
    'citadel_secret_controller_secret_deleted_cert_count': ('citadel.secret_controller.secret_deleted_cert_count'),
    'citadel_secret_controller_svc_acc_created_cert_count': ('citadel.secret_controller.svc_acc_created_cert_count'),
    'citadel_secret_controller_svc_acc_deleted_cert_count': ('citadel.secret_controller.svc_acc_deleted_cert_count'),
    'citadel_server_authentication_failure_count': 'citadel.server.authentication_failure_count',
    'citadel_server_citadel_root_cert_expiry_timestamp': ('citadel.server.citadel_root_cert_expiry_timestamp'),
    'citadel_server_csr_count': 'citadel.server.csr_count',
    'citadel_server_csr_parsing_err_count': 'citadel.server.csr_parsing_err_count',
    'citadel_server_id_extraction_err_count': 'citadel.server.id_extraction_err_count',
    'citadel_server_success_cert_issuance_count': 'citadel.server.success_cert_issuance_count',
    # These metrics supported Istio 1.5
    'galley_validation_config_update_error': 'galley.validation.config_update_error',
    'citadel_server_root_cert_expiry_timestamp': 'citadel.server.root_cert_expiry_timestamp',
    'galley_validation_passed': 'galley.validation.passed',
    'galley_validation_failed': 'galley.validation.failed',
    'pilot_conflict_outbound_listener_http_over_https': 'pilot.conflict.outbound_listener.http_over_https',
    'pilot_inbound_updates': 'pilot.inbound_updates',
    'pilot_k8s_cfg_events': 'pilot.k8s.cfg_events',
    'pilot_k8s_reg_events': 'pilot.k8s.reg_events',
    'pilot_proxy_queue_time': 'pilot.proxy_queue_time',
    'pilot_push_triggers': 'pilot.push.triggers',
    'pilot_xds_eds_all_locality_endpoints': 'pilot.xds.eds_all_locality_endpoints',
    'pilot_xds_push_time': 'pilot.xds.push.time',
    'process_virtual_memory_max_bytes': 'process.virtual_memory_max_bytes',
    'sidecar_injection_requests_total': 'sidecar_injection.requests_total',
    'sidecar_injection_success_total': 'sidecar_injection.success_total',
    'sidecar_injection_failure_total': 'sidecar_injection.failure_total',
    'sidecar_injection_skip_total': 'sidecar_injection.skip_total',
    'istio_mcp_clients_total': 'mcp.clients_total',
    'istio_mcp_request_nacks_total': 'mcp.request.nacks_total',
    'istio_mcp_request_acks_total': 'mcp.request.acks_total',
    'galley_istio_networking_virtualservices': 'galley.istio.networking.virtualservices',
    'galley_istio_networking_destinationrules': 'galley.istio.networking.destinationrules',
    'galley_istio_networking_gateways': 'galley.istio.networking.gateways',
    'galley_istio_authentication_meshpolicies': 'galley.istio.authentication.meshpolicies',
    'galley_source_kube_event_error_total': 'galley.source.kube.event.error_total',
    'galley_source_kube_dynamic_converter_failure_total': 'galley.source.kube.dynamic.converter.failure_total',
    'galley_validation_cert_key_update_errors': 'galley.validation.cert.key.update.errors',
    'galley_validation_http_error': 'galley.validation.http.error',
    'mixer_config_rule_config_errors_total': 'mixer.config.rule.config.errors_total',
    'mixer_config_rule_config_match_error_total': 'mixer.config.rule.config.match.errors_total',
    'mixer_config_unsatisfied_action_handler_total': 'mixer.config.unsatisfied.action.handlers_total',
    'mixer_config_adapter_info_config_errors_total': 'mixer.config.adapter.info.config.errors_total',
    'mixer_config_adapter_info_configs_total': 'mixer.config.adapter.info.configs_total',
    'mixer_config_handler_validation_error_total': 'mixer.config.handler.validation.errors_total',
    'mixer_config_instance_config_errors_total': 'mixer.config.instance.config.errors_total',
    'mixer_handler_handler_build_failures_total': 'mixer.handler.handler.build.failures_total',
    # These don't have much documentation around them aside from being mentioned once
    'mixer_config_rule_config_error_count': 'mixer.config.rule.config.errors',
    'mixer_config_rule_config_match_error_count': 'mixer.config.rule.config.match.errors',
    'mixer_config_unsatisfied_action_handler_count': 'mixer.config.unsatisfied.action.handlers',
    'mixer_config_adapter_info_config_error_count': 'mixer.config.adapter.info.config.errors',
    'mixer_config_handler_validation_error_count': 'mixer.config.handler.validation.errors',
    'mixer_config_instance_config_error_count': 'mixer.config.instance.config.errors',
    'mixer_handler_handler_build_failure_count': 'mixer.handler.handler.build.failures',
}

ISTIOD_VERSION = {'istio_build': {'type': 'metadata', 'label': 'tag', 'name': 'version'}}

# These metrics have a _total suffix, even though they're not counters and should be excluded in the
# construct_metrics_config function.
NON_CONFORMING_METRICS = [
    # Histogram
    'galley_runtime_processor_snapshot_events_total',
    # Gauge
    'galley_runtime_state_type_instances_total',
    'mixer_handler_daemons_total',
]

# Helper function that will strip _total from both the raw metric name and the metric name
def construct_metrics_config(metric_map):
    metrics = []
    for raw_metric_name, metric_name in metric_map.items():
        if raw_metric_name.endswith('_total') and raw_metric_name not in NON_CONFORMING_METRICS:
            raw_metric_name = raw_metric_name[:-6]
            metric_name = metric_name[:-6]

        config = {raw_metric_name: {'name': metric_name}}
        metrics.append(config)

    return metrics