import { sveltify } from '@svelte-preprocess-react';
import { ReactSlot } from '@svelte-preprocess-react/react-slot';
import React from 'react';
import { useFunction } from '@utils/hooks/useFunction';
import { type GetProps, Modal as AModal } from 'antd';

export const Modal = sveltify<
  GetProps<typeof AModal>,
  [
    'cancelButtonProps.icon',
    'cancelText',
    'closable.closeIcon',
    'closeIcon',
    'footer',
    'title',
    'okButtonProps.icon',
    'okText',
  ]
>(
  ({
    slots,
    afterClose,
    afterOpenChange,
    getContainer,
    children,
    modalRender,
    ...props
  }) => {
    const afterOpenChangeFunction = useFunction(afterOpenChange);
    const afterCloseFunction = useFunction(afterClose);
    const getContainerFunction = useFunction(getContainer);
    const modalRenderFunction = useFunction(modalRender);
    return (
      <AModal
        {...props}
        afterOpenChange={afterOpenChangeFunction}
        afterClose={afterCloseFunction}
        okText={slots.okText ? <ReactSlot slot={slots.okText} /> : props.okText}
        okButtonProps={{
          ...(props.okButtonProps || {}),
          icon: slots['okButtonProps.icon'] ? (
            <ReactSlot slot={slots['okButtonProps.icon']} />
          ) : (
            props.okButtonProps?.icon
          ),
        }}
        cancelText={
          slots.cancelText ? (
            <ReactSlot slot={slots.cancelText} />
          ) : (
            props.cancelText
          )
        }
        cancelButtonProps={{
          ...(props.cancelButtonProps || {}),
          icon: slots['cancelButtonProps.icon'] ? (
            <ReactSlot slot={slots['cancelButtonProps.icon']} />
          ) : (
            props.cancelButtonProps?.icon
          ),
        }}
        closable={
          slots['closable.closeIcon']
            ? {
                ...(typeof props.closable === 'object' ? props.closable : {}),
                closeIcon: <ReactSlot slot={slots['closable.closeIcon']} />,
              }
            : props.closable
        }
        closeIcon={
          slots.closeIcon ? (
            <ReactSlot slot={slots.closeIcon} />
          ) : (
            props.closeIcon
          )
        }
        footer={slots.footer ? <ReactSlot slot={slots.footer} /> : props.footer}
        title={slots.title ? <ReactSlot slot={slots.title} /> : props.title}
        modalRender={modalRenderFunction}
        getContainer={
          typeof getContainer === 'string' ? getContainerFunction : getContainer
        }
      >
        {children}
      </AModal>
    );
  }
);

export default Modal;
