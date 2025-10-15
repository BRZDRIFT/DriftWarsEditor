import os

def define_env(env):

    baseUrl = ''

    bGitHub = (os.getenv('GX_GITHUB', 0) == 1)
    if bGitHub:
        baseUrl = '/DriftWarsEditor'

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
