import { sveltify } from '@svelte-preprocess-react';
import { ReactSlot } from '@svelte-preprocess-react/react-slot';
import { useMemo } from 'react';
import { useFunction } from '@utils/hooks/useFunction';
import { renderItems } from '@utils/renderItems';
import { DatePicker as ADatePicker, type GetProps } from 'antd';
import dayjs from 'dayjs';

import { type Item } from './context';

type DatePickerProps = GetProps<typeof ADatePicker>;

function formatDayjs(date: any): dayjs.Dayjs {
  if (Array.isArray(date)) {
    return date.map((d) => {
      return formatDayjs(d) as dayjs.Dayjs;
    }) as unknown as dayjs.Dayjs;
  }
  if (typeof date === 'number') {
    return dayjs(date * 1000);
  }
  return dayjs(date);
}

function formatDate(dates: (dayjs.Dayjs | null | undefined)[] | dayjs.Dayjs) {
  if (Array.isArray(dates)) {
    return dates.map((date) => {
      return date ? date.valueOf() / 1000 : null;
    });
  }
  if (typeof dates === 'object' && dates !== null) {
    return dates.valueOf() / 1000;
  }
  return dates;
}

export const DatePicker = sveltify<
  Omit<DatePickerProps, 'onChange' | 'onPanelChange'> & {
    onChange?: (date: ReturnType<typeof formatDate>, ...args: any[]) => void;
    onPanelChange?: (
      date: ReturnType<typeof formatDate>,
      ...args: any[]
    ) => void;
    onValueChange: (date: ReturnType<typeof formatDate>) => void;
    presetItems: Item[];
  },
  [
    'allowClear.clearIcon',
    'prevIcon',
    'nextIcon',
    'suffixIcon',
    'superNextIcon',
    'superPrevIcon',
    'renderExtraFooter',
  ]
>(
  ({
    slots,
    disabledDate,
    value,
    defaultValue,
    defaultPickerValue,
    pickerValue,
    showTime,
    presets,
    presetItems,
    onChange,
    minDate,
    maxDate,
    cellRender,
    panelRender,
    getPopupContainer,
    onValueChange,
    onPanelChange,
    children,
    elRef,
    ...props
  }) => {
    const disabledDateFunction = useFunction(disabledDate);
    const getPopupContainerFunction = useFunction(getPopupContainer);
    const cellRenderFunction = useFunction(cellRender);
    const panelRenderFunction = useFunction(panelRender);
    const validShowTime = useMemo(() => {
      if (typeof showTime === 'object') {
        return {
          ...showTime,
          defaultValue: showTime.defaultValue
            ? formatDayjs(showTime.defaultValue)
            : undefined,
        };
      }
      return showTime;
    }, [showTime]);
    const validValue = useMemo(() => {
      return value ? formatDayjs(value) : undefined;
    }, [value]);
    const validDefaultValue = useMemo(() => {
      return defaultValue ? formatDayjs(defaultValue) : undefined;
    }, [defaultValue]);
    const validDefaultPickerValue = useMemo(() => {
      return defaultPickerValue ? formatDayjs(defaultPickerValue) : undefined;
    }, [defaultPickerValue]);
    const validPickerValue = useMemo(() => {
      return pickerValue ? formatDayjs(pickerValue) : undefined;
    }, [pickerValue]);
    const validMinDate = useMemo(() => {
      return minDate ? formatDayjs(minDate) : undefined;
    }, [minDate]);
    const validMaxDate = useMemo(() => {
      return maxDate ? formatDayjs(maxDate) : undefined;
    }, [maxDate]);
    return (
      <>
        <div style={{ display: 'none' }}>{children}</div>
        <ADatePicker
          {...props}
          ref={elRef}
          value={validValue}
          defaultValue={validDefaultValue}
          defaultPickerValue={validDefaultPickerValue}
          pickerValue={validPickerValue}
          minDate={validMinDate}
          maxDate={validMaxDate}
          showTime={validShowTime}
          disabledDate={disabledDateFunction}
          getPopupContainer={getPopupContainerFunction}
          cellRender={cellRenderFunction}
          panelRender={panelRenderFunction}
          presets={useMemo(() => {
            return (
              presets ||
              renderItems<NonNullable<DatePickerProps['presets']>[number]>(
                presetItems
              )
            ).map((preset) => {
              return {
                ...preset,
                value: formatDayjs(preset.value),
              };
            });
          }, [presets, presetItems])}
          onPanelChange={(date, ...args) => {
            const formattedDates = formatDate(date);
            onPanelChange?.(formattedDates, ...args);
          }}
          onChange={(date, ...args) => {
            const formattedDate = formatDate(date);
            onChange?.(formattedDate, ...args);
            onValueChange(formattedDate);
          }}
          renderExtraFooter={
            slots.renderExtraFooter
              ? () =>
                  slots.renderExtraFooter ? (
                    <ReactSlot slot={slots.renderExtraFooter} />
                  ) : null
              : props.renderExtraFooter
          }
          prevIcon={
            slots.prevIcon ? (
              <ReactSlot slot={slots.prevIcon} />
            ) : (
              props.prevIcon
            )
          }
          nextIcon={
            slots.nextIcon ? (
              <ReactSlot slot={slots.nextIcon} />
            ) : (
              props.nextIcon
            )
          }
          suffixIcon={
            slots.suffixIcon ? (
              <ReactSlot slot={slots.suffixIcon} />
            ) : (
              props.suffixIcon
            )
          }
          superNextIcon={
            slots.superNextIcon ? (
              <ReactSlot slot={slots.superNextIcon} />
            ) : (
              props.superNextIcon
            )
          }
          superPrevIcon={
            slots.superPrevIcon ? (
              <ReactSlot slot={slots.superPrevIcon} />
            ) : (
              props.superPrevIcon
            )
          }
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

export default DatePicker;