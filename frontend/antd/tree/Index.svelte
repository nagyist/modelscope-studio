<svelte:options accessors={true} />

<script lang="ts">
  import {
    bindEvents,
    importComponent,
  } from '@svelte-preprocess-react/component';
  import {
    getSetSlotParamsFn,
    getSlotContext,
    getSlots,
  } from '@svelte-preprocess-react/slot';
  import type React from 'react';
  import type { Gradio } from '@gradio/utils';
  import cls from 'classnames';
  import { writable } from 'svelte/store';

  const AwaitedTree = importComponent(() => import('./tree'));

  export let gradio: Gradio;
  export let props: Record<string, any> = {};
  const updatedProps = writable(props);
  $: updatedProps.update((prev) => ({ ...prev, ...props }));
  export let _internal: Record<string, any> = {};
  export let as_item: string | undefined;
  // gradio properties
  export let visible = true;
  export let elem_id = '';
  export let elem_classes: string[] = [];
  export let elem_style: React.CSSProperties = {};

  const [mergedProps, update] = getSlotContext({
    gradio,
    props: $updatedProps,
    _internal,
    visible,
    elem_id,
    elem_classes,
    elem_style,
    as_item,
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
    restProps: $$restProps,
  });

  const setSlotParams = getSetSlotParamsFn();
</script>

<!-- $$slots.default and slot fallbacks are not working in gradio -->
{#if $mergedProps.visible}
  {#await AwaitedTree then Tree}
    <Tree
      style={$mergedProps.elem_style}
      className={cls($mergedProps.elem_classes, 'ms-gr-antd-tree')}
      id={$mergedProps.elem_id}
      {...$mergedProps.restProps}
      {...$mergedProps.props}
      {...bindEvents($mergedProps, {
        drag_end: 'dragEnd',
        drag_enter: 'dragEnter',
        drag_leave: 'dragLeave',
        drag_over: 'dragOver',
        drag_start: 'dragStart',
        right_click: 'rightClick',
        load_data: 'loadData',
      })}
      slots={$slots}
      {setSlotParams}
    >
      <slot></slot>
    </Tree>
  {/await}
{/if}
