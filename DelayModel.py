#!/usr/bin/env python
from data_models.traindelay import TrainDelay


def to_delay_dict(record):
    line_components = record["affected_services"]["services"][0]["route_id"].split('-')
    delay_dict = {}
    delay_dict["alert_id"] = record["alert_id"]
    delay_dict["severity"] = record["severity"]
    delay_dict["line"] = line_components[0]
    delay_dict["branch"] = line_components[1] if len(line_components) > 1 else None
    delay_dict["start_time"] = record["effect_periods"][0]["effect_start"] if len(record["effect_periods"]) > 1 else record["created_dt"]
    delay_dict["end_time"] = record["effect_periods"][0]["effect_end"] if len(record["effect_periods"]) > 1 else None
    delay_dict["header_text"] = record["header_text"]
    delay_dict["cause_name"] = record["cause_name"]
    return delay_dict


def to_delay_object(record):
    line_components = record["affected_services"]["services"][0]["route_id"].split('-')
    train_delay = TrainDelay(id=str(record["alert_id"]))
    train_delay.severity = record["severity"]
    train_delay.line = line_components[0]
    train_delay.branch = line_components[1] if len(line_components) > 1 else None
    train_delay.start_time = record["effect_periods"][0]["effect_start"] if len(record["effect_periods"]) > 1 else record["created_dt"]
    train_delay.end_time = record["effect_periods"][0]["effect_end"] if len(record["effect_periods"]) > 1 else None
    train_delay.header_text = record["header_text"]
    train_delay.cause = record["cause_name"]
    return train_delay
