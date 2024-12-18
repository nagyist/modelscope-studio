<svelte:options accessors={true} />

<script lang="ts">
  import { bindEvents } from '@svelte-preprocess-react/component';
  import {
    getSlotContext,
    getSlotKey,
    getSlots,
  } from '@svelte-preprocess-react/slot';
  import type React from 'react';
  import type { Gradio } from '@gradio/utils';
  import cls from 'classnames';
  import { writable } from 'svelte/store';

  import { getItems, getSetItemFn } from '../context';

  export let gradio: Gradio;
  export let props: Record<string, any> = {};
  const updatedProps = writable(props);
  $: updatedProps.update((prev) => ({ ...prev, ...props }));
  export let _internal: {
    layout?: boolean;
    index?: number;
  } = {};

  export let as_item: string | undefined;
  export let label: string;

  // gradio properties
  export let visible = true;
  export let elem_id = '';
  export let elem_classes: string[] = [];
  export let elem_style: React.CSSProperties = {};

  const slotKey = getSlotKey();
  const [mergedProps, update] = getSlotContext({
    gradio,
    props: $updatedProps,
    _internal,
    visible,
    elem_id,
    elem_classes,
    elem_style,
    as_item,
    label,
    restProps: $$restProps,
  });
  const slots = getSlots();
  $: update({
    gradio,
    props: $updatedProps,
    _internal,
    visible,
    elem_id,
    elem_classes,
    elem_style,
    as_item,
    label,
    restProps: $$restProps,
  });
  const setItem = getSetItemFn();
  const { default: items } = getItems();
  $: setItem($slotKey, $mergedProps._internal.index || 0, {
    props: {
      style: $mergedProps.elem_style,
      className: cls(
        $mergedProps.elem_classes,
        $mergedProps.props.type
          ? `ms-gr-antd-menu-item-${$mergedProps.props.type}`
          : 'ms-gr-antd-menu-item',
        $items.length > 0 ? 'ms-gr-antd-menu-item-submenu' : ''
      ),
      id: $mergedProps.elem_id,
      label: $mergedProps.label,
      ...$mergedProps.restProps,
      ...$mergedProps.props,
      ...bindEvents($mergedProps, {
        title_click: 'titleClick',
      }),
    },
    slots: {
      ...$slots,
      icon: {
        el: $slots.icon,
        clone: true,
      },
    },
    children: $items.length > 0 ? $items : undefined,
  });
</script>

{#if $mergedProps.visible}
  <slot></slot>
{/if}

<style>
  :global(.ms-gr-antd-noop-class) {
    display: none;
  }
</style>
