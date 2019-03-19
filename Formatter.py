def formPlayer(gpr_json):
    tmp = gpr_json
    playerData = getKeyValue(tmp,'playerData')
    creation_timestamp_ms = getKeyValue(playerData,'creationTimestampMs')
    username = getKeyValue(playerData, 'username')
    team = getKeyValue(playerData, 'team')
    tutorial_state = getKeyValue(playerData,'tutorialState')
    was_created = getKeyValue(tmp,'was_created')
    banned = getKeyValue(tmp, 'banned')
    warn = getKeyValue(tmp, 'warn')
    warn_message_acknowledged = getKeyValue(tmp, 'warnMessageAcknowledged')
    was_suspended = getKeyValue(tmp, 'wasSuspended')
    suspended_message_acknowledged = getKeyValue(tmp, 'suspendedMessageAcknowledged')
    warn_expire_ms = getKeyValue(tmp, 'warnExpireMs')

    output = {'username': username, 'team':team, 'creationTimestampMs':creation_timestamp_ms, \
              'tutorialState':tutorial_state, 'wasCreated':was_created, 'banned': banned, \
              'warn':warn, 'warnMessageAcknowledged': warn_message_acknowledged, 'wasSuspended': was_suspended, \
              'suspendedMessageAcknowledged': suspended_message_acknowledged, 'warnExpireMs':warn_expire_ms}
    return(output)
