import cromlech as cr

# cr_input = "jpet_store\cromlech\jpet_servicecutter_to_cromlech.yaml"
# cr_input = "cargo_tracking\cromlech\ddd_cromlech.yaml"
cr_input = "trading\cromlech\\trading_cromlech.yaml"
cr_output = [[2, '100011N', '100015P'], [3, 4, 5, 6, 7, '100000P', '100001N', '100002N', '100003N', '100004P', '100005P', '100006P', '100013N', '100014P', '100015R', '100016P'], [0, 1, 9, '100000R', '100007P', '100008P', '100009P', '100010P', '100011P', '100012P', '100013P', '100015R', '100016R'], [8, '100001P', '100002P', '100003P']]







cr.setup(cr_input)

result_only_nums = []
for m in cr_output:
    ops = [x for x in m if isinstance(x, int)]
    attrs = [x for x in m if isinstance(x, str)]
    attrs_num = [int(x[:len(x) - 1]) for x in attrs]
    result_only_nums.append(ops + attrs_num)

cr.elect_primary_replicas(result_only_nums)

cr.format_and_draw_final(cr_output, "trading\service_cutter\leung.html")