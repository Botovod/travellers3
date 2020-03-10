import vk_api

from travelers_project.settings import VK_TOKEN, VK_GROUP_ID


def get_session():
    vk_session = vk_api.VkApi(token=VK_TOKEN)

    return vk_session


def upload_photo(random_object):
    vk_session = get_session()
    path, text = random_object
    if path:
        upload = vk_api.VkUpload(vk_session)
        photo = upload.photo_wall(
            photos=path,
            group_id=VK_GROUP_ID)

        photo_url = 'photo{}_{}'.format(photo[0]['owner_id'], photo[0]['id'])
    else:
        photo_url = ''
    return photo_url, text, vk_session


def create_wall_post(post_data):
    photo, message, vk_session = post_data
    vk = vk_session.get_api()

    attachments = post_data[0]
    if attachments:
        vk.wall.post(
            owner_id='-' + str(VK_GROUP_ID),
            message=message,
            from_group=True,
            attachments=photo)
    else:
        vk.wall.post(
            owner_id='-' + str(VK_GROUP_ID),
            message=message,
            from_group=True)
