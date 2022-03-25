### THIS FILE IS AUTOGENERATED. DO NOT EDIT THIS FILE DIRECTLY ###
import minknow_api
from minknow_api.promethion_device_pb2_grpc import *
import minknow_api.promethion_device_pb2 as promethion_device_pb2
from minknow_api.promethion_device_pb2 import *
from minknow_api._support import MessageWrapper, ArgumentError
import time
import logging
import sys

__all__ = [
    "PromethionDeviceService",
    "WaveformSettings",
    "DeviceSettings",
    "TimingEnginePeriods",
    "PixelBlockSettings",
    "PixelSettings",
    "ChangeDeviceSettingsRequest",
    "ChangeDeviceSettingsResponse",
    "GetDeviceSettingsRequest",
    "GetDeviceSettingsResponse",
    "ChangePixelBlockSettingsRequest",
    "ChangePixelBlockSettingsResponse",
    "GetPixelBlockSettingsRequest",
    "GetPixelBlockSettingsResponse",
    "ChangePixelSettingsRequest",
    "ChangePixelSettingsResponse",
    "GetPixelSettingsRequest",
    "GetPixelSettingsResponse",
    "StreamTemperatureRequest",
    "GetTemperatureResponse",
]

def run_with_retry(method, message, timeout, unwraps, full_name):
    retry_count = 20
    error = None
    for i in range(retry_count):
        try:
            result = MessageWrapper(method(message, timeout=timeout), unwraps=unwraps)
            return result
        except grpc.RpcError as e:
            # Retrying unidentified grpc errors to keep clients from crashing
            retryable_error = (e.code() == grpc.StatusCode.UNKNOWN and "Stream removed" in e.details() or \
                                (e.code() == grpc.StatusCode.INTERNAL and "RST_STREAM" in e.details()))
            if retryable_error:
                logging.info('Bypassed ({}: {}) error for grpc: {}. Attempt {}.'.format(e.code(), e.details(), full_name, i))
            else:
                raise
            error = e
        time.sleep(1)
    raise error


class PromethionDeviceService(object):
    """Interface to control PromethION devices."""
    def __init__(self, channel):
        self._stub = PromethionDeviceServiceStub(channel)
        self._pb = promethion_device_pb2
    def change_device_settings(self, _message=None, _timeout=None, **kwargs):
        """Change the settings which apply to the whole device.

        This RPC is idempotent. It may change the state of the system, but if the requested
        change has already happened, it will not fail because of this, make any additional
        changes or return a different value.

        Args:
            _message (minknow_api.promethion_device_pb2.ChangeDeviceSettingsRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            sampling_frequency (google.protobuf.wrappers_pb2.Int32Value, optional): The number of measurements to take each second.

                Possible values are between 1000, and 10000.
                If the value is outside of this range, it will be clamped within it

                This value cannot be changed during acquisition.
            ramp_voltage (google.protobuf.wrappers_pb2.DoubleValue, optional): The value to apply as the ramp voltage (in millivolts)

                Valid values are in the range -1250mv..1250mv
            bias_voltage (float, optional): The value to apply as the bias voltage (in millivolts)

                Valid values are in the range -1250mv..1250mv
            bias_voltage_waveform (minknow_api.promethion_device_pb2.WaveformSettings, optional): The waveform settings
            saturation_control_enabled (google.protobuf.wrappers_pb2.BoolValue, optional): Enables saturation control on the device
            fast_calibration_enabled (google.protobuf.wrappers_pb2.BoolValue, optional): Enable use of the fast calibration mode across the device
            temperature_target (google.protobuf.wrappers_pb2.FloatValue, optional): If the device is capable (see device.get_device_info().temperature_controllable)
                then this sets the minimum and maximum temperatures of the flow-cell.

                These values must be between the limits specified in the application config,
                see: min_user_setpoint_temperature_celsius and max_user_setpoint_temperature_celsius
            timings (minknow_api.promethion_device_pb2.TimingEnginePeriods, optional): If specified, the device will adopt these timings to set how
                long is spent at various stages of the current digitisation processes.
                The message includes a way of returning to default timings.

                This value cannot be changed during acquisition

        Returns:
            minknow_api.promethion_device_pb2.ChangeDeviceSettingsResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.change_device_settings,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.promethion_device.PromethionDeviceService")

        unused_args = set(kwargs.keys())

        _message = ChangeDeviceSettingsRequest()

        if "sampling_frequency" in kwargs:
            unused_args.remove("sampling_frequency")
            _message.settings.sampling_frequency.value = kwargs['sampling_frequency']

        if "ramp_voltage" in kwargs:
            unused_args.remove("ramp_voltage")
            _message.settings.ramp_voltage.value = kwargs['ramp_voltage']

        if "bias_voltage" in kwargs:
            unused_args.remove("bias_voltage")
            _message.settings.bias_voltage = kwargs['bias_voltage']

        if "bias_voltage_waveform" in kwargs:
            unused_args.remove("bias_voltage_waveform")
            _message.settings.bias_voltage_waveform.CopyFrom(kwargs['bias_voltage_waveform'])

        if "saturation_control_enabled" in kwargs:
            unused_args.remove("saturation_control_enabled")
            _message.settings.saturation_control_enabled.value = kwargs['saturation_control_enabled']

        if "fast_calibration_enabled" in kwargs:
            unused_args.remove("fast_calibration_enabled")
            _message.settings.fast_calibration_enabled.value = kwargs['fast_calibration_enabled']

        if "temperature_target" in kwargs:
            unused_args.remove("temperature_target")
            _message.settings.temperature_target.value = kwargs['temperature_target']

        if "timings" in kwargs:
            unused_args.remove("timings")
            _message.settings.timings.CopyFrom(kwargs['timings'])

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to change_device_settings: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.change_device_settings,
                              _message, _timeout,
                              [],
                              "minknow_api.promethion_device.PromethionDeviceService")
    def get_device_settings(self, _message=None, _timeout=None, **kwargs):
        """Get the current settings which apply to the whole device.

        This RPC has no side effects. Calling it will have no effect on the state of the
        system. It is safe to call repeatedly, or to retry on failure, although there is no
        guarantee it will return the same information each time.

        Args:
            _message (minknow_api.promethion_device_pb2.GetDeviceSettingsRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.

        Returns:
            minknow_api.promethion_device_pb2.GetDeviceSettingsResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_device_settings,
                                  _message, _timeout,
                                  ['settings'],
                                  "minknow_api.promethion_device.PromethionDeviceService")

        unused_args = set(kwargs.keys())

        _message = GetDeviceSettingsRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_device_settings: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_device_settings,
                              _message, _timeout,
                              ['settings'],
                              "minknow_api.promethion_device.PromethionDeviceService")
    def change_pixel_block_settings(self, _message=None, _timeout=None, **kwargs):
        """Change the settings which apply specific pixel blocks.

        This RPC is idempotent. It may change the state of the system, but if the requested
        change has already happened, it will not fail because of this, make any additional
        changes or return a different value.

        Args:
            _message (minknow_api.promethion_device_pb2.ChangePixelBlockSettingsRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            pixel_blocks (minknow_api.promethion_device_pb2.ChangePixelBlockSettingsRequest.PixelBlocksEntry, optional): 1 based map of different pixel blocks settings, a sparse map
                is accepted, keys should be integers between 1 and 12.
            pixel_block_default (minknow_api.promethion_device_pb2.PixelBlockSettings, optional): If supplied, contains settings applied to every block before then
                applying any specific settings in the per block settings.

        Returns:
            minknow_api.promethion_device_pb2.ChangePixelBlockSettingsResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.change_pixel_block_settings,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.promethion_device.PromethionDeviceService")

        unused_args = set(kwargs.keys())

        _message = ChangePixelBlockSettingsRequest()

        if "pixel_blocks" in kwargs:
            unused_args.remove("pixel_blocks")
            for key, value in kwargs['pixel_blocks'].items():
                _message.pixel_blocks[key].CopyFrom(value)

        if "pixel_block_default" in kwargs:
            unused_args.remove("pixel_block_default")
            _message.pixel_block_default.CopyFrom(kwargs['pixel_block_default'])

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to change_pixel_block_settings: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.change_pixel_block_settings,
                              _message, _timeout,
                              [],
                              "minknow_api.promethion_device.PromethionDeviceService")
    def get_pixel_block_settings(self, _message=None, _timeout=None, **kwargs):
        """Get the settings which apply to specific pixel blocks.

        This RPC has no side effects. Calling it will have no effect on the state of the
        system. It is safe to call repeatedly, or to retry on failure, although there is no
        guarantee it will return the same information each time.

        Args:
            _message (minknow_api.promethion_device_pb2.GetPixelBlockSettingsRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.

        Returns:
            minknow_api.promethion_device_pb2.GetPixelBlockSettingsResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_pixel_block_settings,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.promethion_device.PromethionDeviceService")

        unused_args = set(kwargs.keys())

        _message = GetPixelBlockSettingsRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_pixel_block_settings: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_pixel_block_settings,
                              _message, _timeout,
                              [],
                              "minknow_api.promethion_device.PromethionDeviceService")
    def change_pixel_settings(self, _message=None, _timeout=None, **kwargs):
        """Change the settings which apply to the referenced pixels.

        This RPC is idempotent. It may change the state of the system, but if the requested
        change has already happened, it will not fail because of this, make any additional
        changes or return a different value.

        Args:
            _message (minknow_api.promethion_device_pb2.ChangePixelSettingsRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            pixels (minknow_api.promethion_device_pb2.ChangePixelSettingsRequest.PixelsEntry, optional): 1 based map of up to 3000 different pixel settings
            pixel_default (minknow_api.promethion_device_pb2.PixelSettings, optional): If supplied, contains settings applied to every pixel before then
                applying any specific settings in the per pixel settings.

        Returns:
            minknow_api.promethion_device_pb2.ChangePixelSettingsResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.change_pixel_settings,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.promethion_device.PromethionDeviceService")

        unused_args = set(kwargs.keys())

        _message = ChangePixelSettingsRequest()

        if "pixels" in kwargs:
            unused_args.remove("pixels")
            for key, value in kwargs['pixels'].items():
                _message.pixels[key].CopyFrom(value)

        if "pixel_default" in kwargs:
            unused_args.remove("pixel_default")
            _message.pixel_default.CopyFrom(kwargs['pixel_default'])

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to change_pixel_settings: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.change_pixel_settings,
                              _message, _timeout,
                              [],
                              "minknow_api.promethion_device.PromethionDeviceService")
    def get_pixel_settings(self, _message=None, _timeout=None, **kwargs):
        """Get the pixel settings for the requested pixel's

        This RPC has no side effects. Calling it will have no effect on the state of the
        system. It is safe to call repeatedly, or to retry on failure, although there is no
        guarantee it will return the same information each time.

        Args:
            _message (minknow_api.promethion_device_pb2.GetPixelSettingsRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            pixels (int): The channels (one based) to return data for.
                A sparse map is accepted

        Returns:
            minknow_api.promethion_device_pb2.GetPixelSettingsResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_pixel_settings,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.promethion_device.PromethionDeviceService")

        unused_args = set(kwargs.keys())

        _message = GetPixelSettingsRequest()

        if "pixels" in kwargs:
            unused_args.remove("pixels")
            _message.pixels.extend(kwargs['pixels'])
        else:
            raise ArgumentError("get_pixel_settings requires a 'pixels' argument")

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_pixel_settings: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_pixel_settings,
                              _message, _timeout,
                              [],
                              "minknow_api.promethion_device.PromethionDeviceService")
    def stream_temperature(self, _message=None, _timeout=None, **kwargs):
        """Stream the current temperature of the device

        Since 4.3

        This RPC has no side effects. Calling it will have no effect on the state of the
        system. It is safe to call repeatedly, or to retry on failure, although there is no
        guarantee it will return the same information each time.

        Args:
            _message (minknow_api.promethion_device_pb2.StreamTemperatureRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
                Note that this is the time until the call ends, not the time between returned
                messages.
            period_seconds (int, optional): How often temperature updates should be sent
                Defaults to a period of 1 second, if not specified, or set to 0

        Returns:
            iter of minknow_api.promethion_device_pb2.GetTemperatureResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.stream_temperature,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.promethion_device.PromethionDeviceService")

        unused_args = set(kwargs.keys())

        _message = StreamTemperatureRequest()

        if "period_seconds" in kwargs:
            unused_args.remove("period_seconds")
            _message.period_seconds = kwargs['period_seconds']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to stream_temperature: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.stream_temperature,
                              _message, _timeout,
                              [],
                              "minknow_api.promethion_device.PromethionDeviceService")
