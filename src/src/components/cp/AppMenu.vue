<script setup>
import { ref } from 'vue';

import AppMenuItem from './AppMenuItem.vue';

const model = ref([
    {
        label: 'Меню',
        items: [{ label: 'Рабочий стол', icon: 'pi pi-fw pi-home', to: '/' }]
    },
    {
        label: 'Анализ и метрики',
        items: [
            { label: 'Финансы', icon: 'pi pi-fw pi-id-card', to: '/' },
            { label: 'Ресурсы', icon: 'pi pi-fw pi-check-square', to: '/' },
            { label: 'Прогнозирование', icon: 'pi pi-fw pi-bookmark', to: '/' },
        ]
    },
    {
        label: 'Карта',
        items: [
            { label: 'Владивосток', icon: 'pi pi-fw pi-eye', to: '/', badge: 'NEW' },
            { label: 'Сахалин', icon: 'pi pi-fw pi-globe', to: '/', }
        ]
    },

    {
        label: 'Реестры',
        icon: 'pi pi-fw pi-briefcase',
        to: '/pages',
        items: [
            {
                label: 'Парсеры',
                icon: 'pi pi-fw pi-globe',
                to: '/'
            },
            {
                label: 'Пользователи',
                icon: 'pi pi-fw pi-user',

            },

            {
                label: 'График',
                icon: 'pi pi-fw pi-calendar',
                to: '/'
            },
            {
                label: 'Планирование',
                icon: 'pi pi-fw pi-exclamation-circle',
                to: '/'
            },
        ]
    },

    {
        label: 'Get Started',
        items: [
            {
                label: 'Поддержка',
                icon: 'pi pi-fw pi-question',
                to: '/'
            },
        ]
    }
]);
</script>

<template>
    <ul class="layout-menu">
        <template v-for="(item, i) in model" :key="item">
            <app-menu-item v-if="!item.separator" :item="item" :index="i"></app-menu-item>
            <li v-if="item.separator" class="menu-separator"></li>
        </template>
    </ul>
</template>

<style lang="scss" scoped></style>
