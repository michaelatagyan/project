template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>baton_1</class>
 <widget class="QMainWindow" name="baton_1">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>834</width>
    <height>667</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>170</y>
      <width>606</width>
      <height>80</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <widget class="QPushButton" name="Btn_4">
       <property name="text">
        <string>Задание 4</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="Btn_10">
       <property name="text">
        <string>Задание 10</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="Btn_mix">
       <property name="text">
        <string>Задание 19-21</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget_2">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>250</y>
      <width>302</width>
      <height>78</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout_2">
     <item>
      <widget class="QLabel" name="kolvo">
       <property name="text">
        <string>Количество заданий:</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="amount"/>
     </item>
     <item>
      <widget class="QPushButton" name="baton">
       <property name="text">
        <string>Сгенерировать</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget_3">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>320</y>
      <width>180</width>
      <height>80</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout_3">
     <item>
      <widget class="QLabel" name="label">
       <property name="text">
        <string>Генерация для задания: None</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget_4">
    <property name="geometry">
     <rect>
      <x>350</x>
      <y>400</y>
      <width>61</width>
      <height>80</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout_4">
     <item>
      <widget class="QLabel" name="scs">
       <property name="text">
        <string>Успешно!</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget_5">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>560</y>
      <width>279</width>
      <height>80</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout_5">
     <item>
      <widget class="QLabel" name="author_label">
       <property name="text">
        <string>Автор проекта: Атагян Михаил Александрович</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget_6">
    <property name="geometry">
     <rect>
      <x>260</x>
      <y>470</y>
      <width>251</width>
      <height>80</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout_6">
     <item>
      <widget class="QPushButton" name="tool_btn">
       <property name="text">
        <string>Расширенные настройки для 10 задания</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>834</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

template1 = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>40</y>
      <width>452</width>
      <height>80</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout_v1">
     <item>
      <widget class="QPushButton" name="delete_btn">
       <property name="text">
        <string>Добавить свое(и) слово(а)</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="add_btn">
       <property name="text">
        <string>Удалить слово(а)</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton">
       <property name="text">
        <string>Посмотреть базу данных</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>600</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''