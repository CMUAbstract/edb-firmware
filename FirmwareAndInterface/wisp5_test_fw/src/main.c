/**
 * @file       usr.c
 * @brief      WISP application-specific code set
 * @details    The WISP application developer's implementation goes here.
 *
 * @author     Aaron Parks, UW Sensor Systems Lab
 *
 */

#include <msp430.h>
#include "wisp-base.h"
#include "debug.h"

WISP_dataStructInterface_t wispData;

uint32_t wisp_pc;

/** 
 * This function is called by WISP FW after a successful ACK reply
 *
 */
void my_ackCallback (void) {
  asm(" NOP");
}

/**
 * This function is called by WISP FW after a successful read command
 *  reception
 *
 */
void my_readCallback (void) {
  asm(" NOP");
}

/**
 * This function is called by WISP FW after a successful write command
 *  reception
 *
 */
void my_writeCallback (void) {
  asm(" NOP");
}

/** 
 * This function is called by WISP FW after a successful BlockWrite
 *  command decode

 */
void my_blockWriteCallback  (void) {
  asm(" NOP");
}


/**
 * This implements the user application and should never return
 *
 * Must call WISP_init() in the first line of main()
 * Must call WISP_doRFID() at some point to start interacting with a reader
 */
void main(void) {

#ifdef CONFIG_BREAKPOINT_TEST
  uint16_t count = 0;
#endif

  WISP_init();
  debug_setup();
  
  // Register callback functions with WISP comm routines
  WISP_registerCallback_ACK(&my_ackCallback);
  WISP_registerCallback_READ(&my_readCallback);
  WISP_registerCallback_WRITE(&my_writeCallback);
  WISP_registerCallback_BLOCKWRITE(&my_blockWriteCallback);
  
  // Get access to EPC, READ, and WRITE data buffers
  WISP_getDataBuffers(&wispData);
  
  // Set up operating parameters for WISP comm routines
  WISP_setMode( MODE_READ | MODE_WRITE | MODE_USES_SEL); 
  WISP_setAbortConditions(CMD_ID_READ | CMD_ID_WRITE /*| CMD_ID_ACK*/);
  
  // Set up EPC
  wispData.epcBuf[0] = 0x05; // WISP version
  wispData.epcBuf[1] = *((uint8_t*)INFO_WISP_TAGID+1); // WISP ID MSB
  wispData.epcBuf[2] = *((uint8_t*)INFO_WISP_TAGID); // WISP ID LSB
  wispData.epcBuf[3] = 0x33;
  wispData.epcBuf[4] = 0x44;
  wispData.epcBuf[5] = 0x55;
  wispData.epcBuf[6] = 0x66;
  wispData.epcBuf[7] = 0x77;
  wispData.epcBuf[8] = 0x88;
  wispData.epcBuf[9] = 0x99;
  wispData.epcBuf[10]= 0xAA;
  wispData.epcBuf[11]= 0xBB;

#ifdef CONFIG_BREAKPOINT_TEST
  __enable_interrupt();
#endif
  
  // Talk to the RFID reader.
  while (FOREVER) {
#ifdef CONFIG_BREAKPOINT_TEST
    count++;
    if (count % 100 == 0)
        BREAKPOINT(1);
#else
    WISP_doRFID();
#endif
  }
}
