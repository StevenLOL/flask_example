# -*- coding:utf-8 -*-
# @author:Eric Luo
# @file:view.py
# @time:2017/3/13 0013 10:26
def open_excel(file='file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))


# 根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file='file.xls', colnameindex=0, by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数
    colnames = table.row_values(colnameindex)  # 某一行数据
    list = []
    for rownum in range(1, nrows):

        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list


ALLOWED_EXTENSIONS = set(['xls', 'xlsx'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@login_required
@main.route('/import_device', methods=['GET', 'POST'])
def import_device():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename

        # 判断文件名是否合规
        if file and allowed_file(filename):
            file.save(os.path.join('.\\upload', filename))
        else:
            flash('失败:上传文件格式不对')
            return render_template('import_device.html')

        # file.save(os.path.join('c:\\mnt', filename))
        # file.save(os.path.join('.\\upload', filename))

        # 添加到数据库
        tables = excel_table_byindex(file='.\\upload\\' + filename)
        for row in tables:
            # 判断表格式是否对
            if '手持机DEVICEID' not in row or \
                            '手持机SIMID' not in row or \
                            '手持机硬件版本' not in row or \
                            '手持机软件版本' not in row or \
                            '脚扣DEVICEID' not in row or \
                            '脚扣SIMID' not in row or \
                            '脚扣硬件版本' not in row or \
                            '脚扣软件版本' not in row:
                flash('失败:excel表格式不对')
                return render_template('import_device.html')

            # print('0x%04x' % int(str(row['手持机DEVICEID']).split('.')[0], base=16))
            # 判断手持机字段是否存在
            if row['手持机DEVICEID'] != '' and row['手持机SIMID'] != '' and \
                            row['手持机硬件版本'] != '' and row['手持机软件版本'] != '':
                id_format = '0x%04x' % int(str(row['手持机DEVICEID']).split('.')[0], base=16)
                device = Device(device_type='手持机',
                                device_id=id_format,
                                device_simid=str(row['手持机SIMID']).split('.')[0],
                                hard_version=int(row['手持机硬件版本']),
                                soft_version=int(row['手持机软件版本']),
                                warehouse=False,
                                shipment_time='无',
                                agent='无',
                                prison='无',
                                shutdown=False)
                # 判断是否id重复
                flag = True
                if Device.query.filter_by(device_id=device.device_id).count() > 0:
                    flash('失败:设备ID:%s已存在' % device.device_id)
                    flag = False
                # 判断simid是否重复
                elif Device.query.filter_by(device_simid=device.device_simid).count() > 0:
                    flash('失败:设备SIMID:%s已存在' % device.device_simid)
                    flag = False
                if flag:
                    db.session.add(device)
                else:
                    return render_template('import_device.html')

            if row['脚扣DEVICEID'] != '' and row['脚扣SIMID'] != '' and \
                            row['脚扣硬件版本'] != '' and row['脚扣软件版本'] != '':
                id_format = '0x%04x' % int(str(row['脚扣DEVICEID']).split('.')[0], base=16)
                device = Device(device_type='脚扣',
                                device_id=id_format,
                                device_simid=str(row['脚扣SIMID']).split('.')[0],
                                hard_version=int(row['脚扣硬件版本']),
                                soft_version=int(row['脚扣软件版本']),
                                warehouse=False,
                                shipment_time='无',
                                agent='无',
                                prison='无',
                                shutdown=False)
                # 判断是否id重复
                flag = True
                if Device.query.filter_by(device_id=device.device_id).count() > 0:
                    flash('失败:设备ID:%s已存在' % device.device_id)
                    flag = False
                # 判断simid是否重复
                elif Device.query.filter_by(device_simid=device.device_simid).count() > 0:
                    flash('失败:设备SIMID:%s已存在' % device.device_simid)
                    flag = False
                if flag:
                    db.session.add(device)
                else:
                    return render_template('import_device.html')
        return redirect(url_for('.index'))

    return render_template('import_device.html')
