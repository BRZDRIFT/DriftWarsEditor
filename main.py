def define_env(env):

    baseUrl = env.variables.get('base_url', '')

    @env.macro
    def fn(fnName):
        return '[' + fnName +']('+baseUrl+'/driftScript/functions/#' + fnName.lower() +')'

    @env.macro
    def enum(enumName):
        return '[' + enumName +']('+baseUrl+'/driftScript/enumerations/#' + enumName.lower() +')'

    @env.macro
    def entry(entryName):
        return '[' + entryName +']('+baseUrl+'/driftScript/scriptEntryPoints/#' + entryName.lower() +')'

    @env.macro
    def eventQueue():
        return '[Event Queue]('+baseUrl+'/driftScript/eventQueue/#event_queue)'

    @env.macro
    def type(typeName):
        return '[' + typeName + ']('+baseUrl+'/driftScript/builtinTypes/#'+typeName.lower()+')'
