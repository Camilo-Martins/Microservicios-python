import { ref } from 'vue'

const show = ref(false)
const message = ref('')
const type = ref('error') // error | success | info

export default function useToast() {
  const trigger = (msg, toastType = 'error', timeout = 3000) => {
    message.value = msg
    type.value = toastType
    show.value = true

    setTimeout(() => {
      show.value = false
    }, timeout)
  }

  return {
    show,
    message,
    type,
    trigger
  }
}
