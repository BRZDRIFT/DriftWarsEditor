def define_env(env):

    @env.macro
    def fn(fnName):
        baseUrl = env.variables.get('base_url', '')
        return '[' + fnName +']('+baseUrl+'/driftScript/functions/#' + fnName.lower() +')'

    @env.macro
    def enum(enumName):
        baseUrl = env.variables.get('base_url', '')
        return '[' + enumName +']('+baseUrl+'/driftScript/enumerations/#' + enumName.lower() +')'

    @env.macro
    def entry(entryName):
        baseUrl = env.variables.get('base_url', '')
        return '[' + entryName +']('+baseUrl+'/driftScript/scriptEntryPoints/#' + entryName.lower() +')'

    @env.macro
    def eventQueue():
        baseUrl = env.variables.get('base_url', '')
        return '[Event Queue]('+baseUrl+'/driftScript/eventQueue/#event_queue)'

    @env.macro
    def type(typeName):
        baseUrl = env.variables.get('base_url', '')
        return '[' + typeName + ']('+baseUrl+'/driftScript/builtinTypes/#'+typeName.lower()+')'
