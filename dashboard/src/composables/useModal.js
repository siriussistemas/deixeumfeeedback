import bus from '@/utils/bus';

const EVENT_NAME = 'modal:toggle';


export default function useModal() {
  const open = (payload={}) => {
    bus.emit(EVENT_NAME, {status: true, ...payload});
  };

  const close = (payload={}) => {
    bus.emit(EVENT_NAME, {status: false, ...payload});
  };

  const listen = (callback) => {
    bus.on(EVENT_NAME, callback);
  };

  const off = (callback) => {
    bus.off(EVENT_NAME, callback);
  };

  return { open, close, listen, off }
}