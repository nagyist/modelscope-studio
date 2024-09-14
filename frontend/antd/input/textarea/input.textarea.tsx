import { sveltify } from '@svelte-preprocess-react';
import { ReactSlot } from '@svelte-preprocess-react/react-slot';
import { useFunction } from '@utils/hooks/useFunction';
import { type GetProps, Input as AInput } from 'antd';

export const InputTextarea = sveltify<
  GetProps<typeof AInput.TextArea> & {
    onValueChange: (value: string) => void;
  },
  ['allowClear.clearIcon']
>(
  ({
    slots,
    children,
    count,
    showCount,
    onValueChange,
    onChange,
    elRef,
    ...props
  }) => {
    const countStrategyFunction = useFunction(count?.strategy);
    const countExceedFormatterFunction = useFunction(count?.exceedFormatter);
    const countShowFunction = useFunction(count?.show);
    const showCountFunction = useFunction(
      typeof showCount === 'object' ? showCount.formatter : undefined
    );

    return (
      <>
        <div style={{ display: 'none' }}>{children}</div>
        <AInput.TextArea
          {...props}
          ref={elRef}
          onChange={(e) => {
            onChange?.(e);
            onValueChange(e.target.value);
          }}
          showCount={
            typeof showCount === 'object' && showCountFunction
              ? {
                  formatter: showCountFunction,
                }
              : showCount
          }
          count={{
            ...count,
            exceedFormatter: countExceedFormatterFunction,
            strategy: countStrategyFunction,
            show: countShowFunction || count?.show,
          }}
          allowClear={
            slots['allowClear.clearIcon']
              ? {
                  clearIcon: <ReactSlot slot={slots['allowClear.clearIcon']} />,
                }
              : props.allowClear
          }
        />
      </>
    );
  }
);

export default InputTextarea;