from wrapper_qpy.decorators import static_vars



def CL_WriteConfiguration()
    pass


@static_vars(isdown=False)
def CL_Shutdown():
    if CL_Shutdown.isdown:
        print("recursive shutdown")
        return
    CL_Shutdown.isdown = True
    CL_WriteConfiguration()
