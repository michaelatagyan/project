template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>baton_1</class>
 <widget class="QMainWindow" name="baton_1">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>758</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="gridLayoutWidget">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>200</y>
      <width>250</width>
      <height>91</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout">
     <item row="0" column="0">
      <widget class="QPushButton" name="Btn_4">
       <property name="text">
        <string>Задание 4</string>
       </property>
      </widget>
     </item>
     <item row="0" column="2">
      <widget class="QPushButton" name="Btn_mix">
       <property name="text">
        <string>Задание 19-21</string>
       </property>
      </widget>
     </item>
     <item row="0" column="1">
      <widget class="QPushButton" name="Btn_10">
       <property name="text">
        <string>Задание 10</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QLineEdit" name="amount">
    <property name="geometry">
     <rect>
      <x>360</x>
      <y>310</y>
      <width>51</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="baton">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>310</y>
      <width>101</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Сгенерировать</string>
    </property>
   </widget>
   <widget class="QLabel" name="kolvo">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>310</y>
      <width>131</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Количество заданий:</string>
    </property>
   </widget>
   <widget class="QLabel" name="scs">
    <property name="geometry">
     <rect>
      <x>310</x>
      <y>380</y>
      <width>61</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Успешно!</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>270</x>
      <y>350</y>
      <width>161</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Генерация для задания: None</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>758</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''