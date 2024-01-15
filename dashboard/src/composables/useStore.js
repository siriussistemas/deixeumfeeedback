import store from '@/store';

export default function useStore(module) {
  if(module){
    return store[module];
  }

  return store;
}