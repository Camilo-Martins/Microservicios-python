<script setup>
import { ref, onMounted } from 'vue';
import BaseButton from '@/components/BaseButton.vue';
import useToast from '@/stores/useToast';
import { useAddHorario } from '../composables/useHorario';

const { trigger } = useToast()
const { sendData, loading, error, data } = useAddHorario()

const emit = defineEmits(['created'])


const submit = async () => {
    
  try {
      await sendData()

    emit('created');
  } catch (error) {
     trigger(error)
  }
   


};
</script>

<template>

    <!-- Formulario -->
    <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-5 mb-8">
        <form @submit.prevent="submit"
            class="grid grid-cols-1 md:grid-cols-7 gap-4 items-end">

            <BaseButton label="Agregar Personal" type="submit">
                Crear Horario
            </BaseButton>

        </form>
       
    </div>

</template>

<style scoped></style>
