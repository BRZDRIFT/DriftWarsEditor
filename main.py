def define_env(env):

    @env.macro
    def fn(fnName):
        return '[' + fnName +'](/driftScript/functions/#' + fnName.lower() +')'

    @env.macro
    def enum(enumName):
        return '[' + enumName +'](/driftScript/enumerations/#' + enumName.lower() +')'

    @env.macro
    def entry(entryName):
        return '[' + entryName +'](/driftScript/scriptEntryPoints/#' + entryName.lower() +')'

    @env.macro
    def eventQueue():
        return '[Event Queue](/driftScript/eventQueue/#event_queue)'

    @env.macro
    def type(typeName):
        return '[' + typeName + '](/driftScript/builtinTypes/#'+typeName.lower()+')'
