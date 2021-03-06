#ifndef HOST_COMM_IMPL_H
#define HOST_COMM_IMPL_H

#include <stdint.h>

#include "host_comm.h"
#include "interrupt.h"

#define HOST_MSG_BUF_SIZE       64 // buffer for UART messages (to host) for main loop

// TODO: prefix names with host_comm

void send_voltage(uint16_t voltage);
void send_return_code(unsigned code);
void send_interrupt_context(interrupt_context_t *int_context);
void send_param(param_t param);
void send_echo(uint8_t value);
void forward_msg_to_host(unsigned descriptor, uint8_t *buf, unsigned len);

#endif

