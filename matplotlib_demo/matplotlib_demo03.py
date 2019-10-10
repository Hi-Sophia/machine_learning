import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
'''
subplot多合一显示
'''
#均匀图中图,不均匀图中图
# plt.figure()
#
# #plt.subplot(2,2,1)表示将整个图像窗口分为2行2列, 当前位置为1
# plt.subplot(2,2,1)
# plt.plot([0,1],[0,1])
#
# plt.subplot(2,2,2)
# plt.plot([0,1],[0,2])
#
#
# plt.subplot(223)
# plt.plot([0,1],[0,3])
#
#
# plt.subplot(224)
# plt.plot([0,1],[0,4])
#
# plt.show()

'''
plt.subplot2grid
来创建第1个小图, 
(3,3)表示将整个图像窗口分成3行3列, 
(0,0)表示从第0行第0列开始作图，
colspan=3表示列的跨度为3, rowspan=1表示行的跨度为1. colspan和rowspan缺省, 默认跨度为1
'''
# ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
# ax1.plot([1, 2], [1, 2])    # 画小图
# ax1.set_title('ax1_title')  # 设置小图的标题
#
#
# ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
# ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
#
#
# ax4 = plt.subplot2grid((3, 3), (2, 0))
# ax4.scatter([1, 2], [2, 2])
# ax4.set_xlabel('ax4_x')
# ax4.set_ylabel('ax4_y')
#
# ax5 = plt.subplot2grid((3, 3), (2, 1))
#
# plt.show()


'''
gridspec
'''
# plt.figure()
# gs = gridspec.GridSpec(3, 3)
#
# ax6 = plt.subplot(gs[0, :])
# ax7 = plt.subplot(gs[1, :2])
# ax8 = plt.subplot(gs[1:, 2]) #表示这个图占第1行后的所有行和第2列
# ax9 = plt.subplot(gs[-1, 0]) #表示这个图占倒数第1行和第0列
# ax10 = plt.subplot(gs[-1, -2]) #表示这个图占倒数第1行和倒数第2列.
#
# plt.show()


'''
subplots
'''
f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1,2], [1,2])
plt.show()