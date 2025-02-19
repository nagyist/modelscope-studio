<svelte:options accessors={true} />

<script lang="ts">
  import {
    bindEvents,
    importComponent,
  } from '@svelte-preprocess-react/component';
  import {
    getSetSlotParamsFn,
    getSlotContext,
    getSlotKey,
    getSlots,
  } from '@svelte-preprocess-react/slot';
  import type React from 'react';
  import type { Gradio } from '@gradio/utils';
  import cls from 'classnames';
  import { writable } from 'svelte/store';

  const AwaitedSuggestionItem = importComponent(
    () => import('./suggestion.item')
  );
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
  export let value: string;
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
    value,
    restProps: $$restProps,
  });
  const setSlotParams = getSetSlotParamsFn();
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
    value,
    restProps: $$restProps,
  });

  $: itemProps = {
    props: {
      style: $mergedProps.elem_style,
      className: cls($mergedProps.elem_classes, 'ms-gr-antd-suggestion-item'),
      id: $mergedProps.elem_id,
      label: $mergedProps.label,
      value: $mergedProps.value,
      ...$mergedProps.restProps,
      ...$mergedProps.props,
      ...bindEvents($mergedProps),
    },
    slots: {
      ...$slots,
      extra: {
        el: $slots.extra,
        clone: true,
        callback: setSlotParams,
      },
      icon: {
        el: $slots.icon,
        clone: true,
        callback: setSlotParams,
      },
      label: {
        el: $slots.label,
        clone: true,
        callback: setSlotParams,
      },
    },
  };
</script>

{#if $mergedProps.visible}
  {#await AwaitedSuggestionItem then SuggestionItem}
    <SuggestionItem
      {...itemProps.props}
      slots={itemProps.slots}
      itemIndex={$mergedProps._internal.index || 0}
      itemSlotKey={$slotKey}
    >
      <slot></slot>
    </SuggestionItem>
  {/await}
{/if}
