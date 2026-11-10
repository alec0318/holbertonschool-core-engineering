#!/usr/bin/env python3
def safe_print_division(a, b):
    try: 
        result = a / b
        
    except Exception: 
        result = None

    finally: 
        print(f"Inside result: {result}")

    return result
