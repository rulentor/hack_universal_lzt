<script setup lang="ts">
const props = defineProps<{ name: string }>()
const router = useRouter()
const user = useUserStore()

watchEffect(() => {
  user.setNewName(props.name)
})
</script>

<template>
  <div>
    <div text-4xl>
      <div i-carbon-pedestrian inline-block />
    </div>
    <p>
      intro-hi {{ { name: props.name } }}
    </p>

    <p text-sm opacity-75>
      <em>intro-dynamic-route</em>
    </p>

    <template v-if="user.otherNames.length">
      <p mt-4 text-sm>
        <span opacity-75>intro-aka:</span>
        <ul>
          <li v-for="otherName in user.otherNames" :key="otherName">
            <RouterLink :to="`/hi/${otherName}`" replace>
              {{ otherName }}
            </RouterLink>
          </li>
        </ul>
      </p>
    </template>

    <div>
      <button
        m="3 t6" text-sm btn
        @click="router.back()"
      >
        button-back
      </button>
    </div>
  </div>
</template>
